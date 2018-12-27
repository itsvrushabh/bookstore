from base.serializers import *
from base.models import *
from rest_framework.generics import ListAPIView


class BooksList(ListAPIView):
    """
        Student ListAPIView we can use either queryset or get_queryset()
        to return queryset
        Similarly for serializer_class or override get_serializer_class()
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer

