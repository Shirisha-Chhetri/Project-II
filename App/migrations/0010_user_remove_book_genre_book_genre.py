# Generated by Django 4.0.1 on 2022-03-29 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_delete_reader'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='App.Genre'),
        ),
    ]
