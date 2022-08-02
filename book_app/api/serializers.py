from rest_framework import serializers

from book_app.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Book
        fields=('name','author','price')