# Generated by Django 4.0.1 on 2022-04-14 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0034_alter_book_genre_alter_genre_title_delete_bookgenre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
