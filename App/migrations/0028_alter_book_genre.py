# Generated by Django 4.0.1 on 2022-04-05 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0027_book_genre_alter_book_image_alter_book_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=500),
        ),
    ]
