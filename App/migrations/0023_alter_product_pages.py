# Generated by Django 4.0.1 on 2022-04-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pages',
            field=models.CharField(max_length=100),
        ),
    ]
