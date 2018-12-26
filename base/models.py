from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField()


class Author(models.Model):
    id = models.AutoField()


class SubGenre(models.Model):
    id = models.AutoField()


class Genre(models.Model):
    id = models.AutoField()