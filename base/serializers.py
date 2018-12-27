from rest_framework import serializers
from .models import Author, Book, Genre, SubGenre


# Serializers define the API representation.
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_name', 'author_rating', 'about_the_author', 'sub_genre')


class SubGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubGenre
        fields = ('name', 'description', 'slug', 'genre')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'genre_details', 'slug', 'meta_data')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'status', 'cost', 'currency', 'publish_date_time', 'author')


