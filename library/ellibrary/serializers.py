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
            # Для художественных произведений, которые не переведены, ничего не делаем
            pass
        elif book_type == 'textbook':
            # Для учебников проверяем некоторые поля
            title = data.get('title', None)
            author = data.get('author', None)
            publisher = data.get('publisher', None)
            year_of_release = data.get('yearOfRel', None)

            # Проверяем, чтобы эти 4 поля не повторялись с другими учебниками
            existing_textbooks = Book.objects.filter(
                type='textbook',
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
