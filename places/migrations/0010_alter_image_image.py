# Generated by Django 4.0.5 on 2022-06-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Картинка'),
        ),
    ]
