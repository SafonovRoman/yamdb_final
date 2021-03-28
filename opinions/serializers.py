from rest_framework import serializers
from django.shortcuts import get_object_or_404

from titles.models import Title

from .models import Comment, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    title = serializers.SlugRelatedField(read_only=True,
                                         slug_field='name')

    def validate(self, data):
        user = self.context['request'].user
        title = get_object_or_404(
            Title,
            pk=self.context['view'].kwargs.get('title_id')
        )
        has_review = Review.objects.filter(author=user, title=title).exists()
        if self.context['request'].method == 'POST' and has_review:
            raise serializers.ValidationError(f'Вы уже публиковали ревью на {title}')
        return data

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    review = serializers.SlugRelatedField(read_only=True,
                                          slug_field='id')

    class Meta:
        fields = '__all__'
        model = Comment
