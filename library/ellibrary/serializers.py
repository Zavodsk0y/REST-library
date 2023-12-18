from rest_framework import serializers

from .models import *


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate(self, data):
        book_type = data.get('type', None)
        is_translated = data.get('is_translated', False)

        if book_type == 'fiction' and is_translated == False:
            pass
        elif book_type == 'manual':
            title = data.get('title', None)
            author = data.get('author', None)
            publisher = data.get('publisher', None)
            year_of_release = data.get('yearOfRel', None)

            existing_textbooks = Book.objects.filter(
                type='manual',
                title=title,
                author=author,
                publisher=publisher,
                yearOfRel=year_of_release
            )

            if existing_textbooks.exists():
                raise serializers.ValidationError('Данный учебник уже существует в базе данных.')

        return data


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
