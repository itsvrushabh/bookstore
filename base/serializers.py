from rest_framework import serializers
from .models import Author, Book, Genre, SubGenre


# Serializers define the API representation.
class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = ('name', 'status', 'cost', 'currency', 'publish_date_time', 'auther')


class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ('author_name', 'author_rating', 'about_the_author', 'sub_genre')


class SubGenreSerializer(serializers.Serializer):
    class Meta:
        model = SubGenre
        fields = ('name', 'description', 'slug', 'genre')


class GenreSerializer(serializers.Serializer):
    class Meta:
        model = Genre
        fields = ('name', 'genre_details', 'slug', 'meta_data')