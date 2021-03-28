from datetime import datetime

from django.core.validators import MaxValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория',
                            db_index=True)
    slug = models.SlugField(unique=True,
                            verbose_name='Идентификатор категории',
                            db_index=True)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name='Жанр',
                            db_index=True)
    slug = models.SlugField(unique=True, verbose_name='Идентификатор жанра',
                            db_index=True)

    class Meta:
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название',
                            db_index=True)
    year = models.PositiveSmallIntegerField(
        verbose_name='Год выпуска',
        db_index=True,
        validators=[MaxValueValidator(datetime.today().year)])

    description = models.TextField(verbose_name='Описание',
                                   null=True,
                                   blank=True)
    genre = models.ManyToManyField(Genre,
                                   verbose_name='Жанр',
                                   related_name='titles')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='Категория',
                                 related_name='titles')

    class Meta:
        verbose_name_plural = 'Произведения'
        verbose_name = 'Произведение'

    def __str__(self):
        return self.name
