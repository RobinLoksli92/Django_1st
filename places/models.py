from django.conf import settings
from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    name = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    long = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField('Картинка', null=True)
    number = models.IntegerField('Номер картинки', default=1)
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='images',
        related_name='Картинка',
        null=True
    )

    def __str__(self):
        return f'{self.place}_{self.number}'

    class Meta:
        ordering = ['number']