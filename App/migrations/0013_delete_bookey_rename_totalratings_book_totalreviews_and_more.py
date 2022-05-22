# Generated by Django 4.0.1 on 2022-04-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_bookey'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bookey',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='totalratings',
            new_name='totalreviews',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.TextField(blank=True, null=True),
        ),
    ]
