# Generated by Django 4.1 on 2022-09-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cineTec_app', '0009_pelicula_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='capacidad',
            field=models.IntegerField(default=75),
            preserve_default=False,
        ),
    ]
