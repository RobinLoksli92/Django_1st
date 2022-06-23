from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import os
from places.models import Place, Image
import requests
from urllib.parse import urlparse


class Command(BaseCommand):
    help = 'Places loading'

    def add_arguments(self, parser):
        parser.add_argument('link', type=str)

    def handle(self, *args, **options):
        link = options['link']
        response = requests.get(link)
        response.raise_for_status()
        place_raw = response.json()
        place, created = Place.objects.get_or_create(
            name=place_raw['title'],
            description_short=place_raw['description_short'],
            description_long=place_raw['description_long'],
            long=place_raw['coordinates']['lng'],
            lat=place_raw['coordinates']['lat']
        )
        place_imgs = place_raw['imgs']

        for number, img_url in enumerate(place_imgs, 1):
            img_path = urlparse(img_url).path
            img_name = os.path.basename(img_path)
            response = requests.get(img_url)
            response.raise_for_status()
            img_content = ContentFile(response.content)
            image, created = Image.objects.get_or_create(
                number=number,
                place=place
            )
            image.image.save(img_name, img_content, save=True)
