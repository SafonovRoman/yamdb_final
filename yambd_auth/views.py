from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken

from api_yamdb.settings import AUTHENTICATION_EMAIL_ADDRESS
from yambd_auth.models import User
from yambd_auth.permissions import IsAdmin, IsSelfOrSuper
from yambd_auth.serializers import (ConfirmationCodeSerializer,
                                    EmailSerializer, UserSerializer)


@api_view(['POST'])
def auth_send_code(request):
    serializer = EmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user, created = User.objects.get_or_create(email=serializer.data['email'])
    random_key = default_token_generator.make_token(user)
    user.confirmation_code = random_key
    user.save()
    send_mail(
        subject='Yamdb activation code',
        message=f'Ваш код авторизации для получения токена:\n{random_key}',
        recipient_list=[user.email],
        from_email=AUTHENTICATION_EMAIL_ADDRESS
    )
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['POST'])
def auth_confirm(request):
    serializer = ConfirmationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(User, email=serializer.data['email'])
    if user.confirmation_code == request.data['confirmation_code']:
        token = AccessToken.for_user(user)
        data = {'token': str(token)}
        return Response(data, status.HTTP_200_OK)
    error_msg = 'Неверный код подтверждения email'
    return Response({'confirmation_code': error_msg},
                    status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated, IsAdmin]

    @action(detail=False, methods=['GET', 'PATCH'],
            permission_classes=[IsAuthenticated, IsSelfOrSuper])
    def me(self, request, pk=None):
        if request.method == 'GET':
            return Response(UserSerializer(instance=request.user).data,
                            status.HTTP_200_OK)
        serializer = UserSerializer(instance=request.user,
                                    data=request.data,
                                    partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
