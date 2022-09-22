# Generated by Django 4.1 on 2022-09-21 21:10

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cineTec_app', '0006_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
