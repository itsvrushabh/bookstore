from django.contrib import admin
from base.models import Book, Genre, SubGenre, Author
# Register your models here.
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(SubGenre)
admin.site.register(Author)
