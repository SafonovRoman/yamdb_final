from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from titles.models import Title
from yambd_auth.permissions import PostRegisteredEditOwnerOrSuperOrReadOnly

from .models import Comment, Review
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [PostRegisteredEditOwnerOrSuperOrReadOnly]

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            pk=serializer.context['view'].kwargs.get('title_id')
        )
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [PostRegisteredEditOwnerOrSuperOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(review__id=self.kwargs.get('review_id'))

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            pk=serializer.context['view'].kwargs.get('review_id')
        )
        serializer.save(author=self.request.user, review=review)
