from django.db import models
from datetime import datetime


# Create your models here.
class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 300)
    genre_details = models.TextField()
    slug = models.CharField(max_length = 300)
    meta_data = models.CharField(max_length = 300)


class SubGenre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 300)
    description = models.TextField()
    slug = models.CharField(max_length = 300)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length = 300)
    author_rating = models.FloatField(null=False, blank=False, default=0.0)
    about_the_author = models.TextField()
    sub_genre = models.ForeignKey(SubGenre, on_delete=models.CASCADE)


class Book(models.Model):
    STATUS_TYPE = (
        ('P', 'Published'),
        ('U', 'Unpublished'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 300)
    status = models.CharField(max_length=1, choices=STATUS_TYPE)
    cost = models.DecimalField(max_digits=8, decimal_places=3)
    currency = models.CharField(max_length = 300)
    publish_date_time = models.DateTimeField(default=datetime.now(), blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
