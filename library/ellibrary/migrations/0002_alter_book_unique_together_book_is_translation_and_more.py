# Generated by Django 4.2.8 on 2023-12-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ellibrary', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='book',
            name='is_translation',
            field=models.BooleanField(default=False, verbose_name='Переведенная книга'),
        ),
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.CharField(choices=[('manual', 'Учебник'), ('fiction', 'Художественная литература')], default='Учебник', max_length=10, verbose_name='Тип книги'),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'author', 'yearOfRel', 'publisher', 'type')},
        ),
    ]
