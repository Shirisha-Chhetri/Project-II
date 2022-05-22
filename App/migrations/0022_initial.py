# Generated by Django 4.0.1 on 2022-04-05 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App', '0021_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('genre', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.CharField(max_length=150)),
                ('bookformat', models.CharField(max_length=150)),
                ('isbn', models.CharField(max_length=150)),
                ('pages', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
