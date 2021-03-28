from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from titles.models import Title
from yambd_auth.models import User


class Review(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='reviews')
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              related_name='reviews')
    score = models.PositiveSmallIntegerField(default=1,
                                             validators=[
                                                 MaxValueValidator(10),
                                                 MinValueValidator(1)
                                             ]
                                             )

    class Meta:
        ordering = ['-pub_date']
        unique_together = ('author', 'title')

    def __str__(self):
        return self.text[:100]


class Comment(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')
    review = models.ForeignKey(Review,
                               on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField('Дата добавления',
                                    auto_now_add=True,
                                    db_index=True)

    class Meta:
        ordering = ['-pub_date']
