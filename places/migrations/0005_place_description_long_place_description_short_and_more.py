# Generated by Django 4.0.5 on 2022-06-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_image_remove_place_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description_long',
            field=models.TextField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.AddField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='place',
            name='lat',
            field=models.FloatField(default=0, verbose_name='Широта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='long',
            field=models.FloatField(default=0, verbose_name='Долгота'),
            preserve_default=False,
        ),
    ]