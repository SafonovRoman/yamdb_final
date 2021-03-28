from rest_framework import serializers

from yambd_auth.models import User


class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=User.UserType.choices)

    class Meta:
        fields = ('first_name', 'last_name',
                  'username', 'bio', 'email', 'role')
        model = User


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(max_length=50)
