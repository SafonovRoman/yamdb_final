from django.contrib.auth import get_user_model
from django.db.models import Avg
from rest_framework import filters, mixins, viewsets

from titles.filters import TitleFilter
from yambd_auth.permissions import IsAdminOrReadOnly

from .models import Category, Genre, Title
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer

User = get_user_model()


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score')
                                      ).order_by('name')
    filterset_class = TitleFilter
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly]


class ListCreateDestroy(mixins.DestroyModelMixin,
                        mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    filter_backends = [filters.SearchFilter]
    lookup_field = 'slug'
    search_fields = ('name',)
    permission_classes = [IsAdminOrReadOnly]


class CategoryViewSet(ListCreateDestroy):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class GenreViewSet(ListCreateDestroy):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
