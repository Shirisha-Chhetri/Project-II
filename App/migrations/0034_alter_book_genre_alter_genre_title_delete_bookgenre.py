# Generated by Django 4.0.1 on 2022-04-14 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0033_bookgenre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.genre', to_field='title'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.DeleteModel(
            name='BookGenre',
        ),
    ]
