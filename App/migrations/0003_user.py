# Generated by Django 4.0.1 on 2022-02-28 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('contact', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('password', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
