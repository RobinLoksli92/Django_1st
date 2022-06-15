from distutils.command.upload import upload
from itertools import count
from django.conf import settings
from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    long = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField('Картинка', null=True, upload_to=settings.MEDIA_ROOT)
    number = models.IntegerField('Номер картинки', blank=True)

    def __str__(self):
        return f'{self.number}'