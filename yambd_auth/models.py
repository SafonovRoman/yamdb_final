from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class UserType(models.TextChoices):
        USER = 'user', _('Пользователь')
        MODERATOR = 'moderator', _('Модератор')
        ADMIN = 'admin', _('Администратор')

    email = models.EmailField(unique=True, blank=False, null=False)
    bio = models.CharField(max_length=1000, blank=True)
    role = models.CharField(choices=UserType.choices,
                            default=UserType.USER,
                            max_length=13)
    confirmation_code = models.CharField(max_length=50, null=True)
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
        null=True
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['pk']

    @property
    def is_admin(self):
        return self.role == self.UserType.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.UserType.MODERATOR
