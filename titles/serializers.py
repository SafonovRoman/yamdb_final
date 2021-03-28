from rest_framework import serializers

from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id',)


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(many=True,
                                         queryset=Genre.objects.all(),
                                         slug_field='slug')

    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            slug_field='slug')

    class Meta:
        model = Title
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TitleSerializer, self).__init__(*args, **kwargs)
        if self.context['request'].method in ['GET']:
            self.fields['genre'] = GenreSerializer(many=True)
            self.fields['category'] = CategorySerializer(read_only=True)
            self.fields['rating'] = serializers.ReadOnlyField()
