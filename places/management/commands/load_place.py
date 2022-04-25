from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Place, PlaceImage

import requests


class Command(BaseCommand):
    help = 'Add place from json file'

    def add_arguments(self, parser):
        parser.add_argument('file_link', type=str)

    def handle(self, *args, **options):
        file_link = options['file_link']
        response = requests.get(file_link)
        place_data = response.json()
        new_place, created = Place.objects.get_or_create(
            title=place_data['title'],
            description_short=place_data['description_short'],
            description_long=place_data['description_long'],
            lng=place_data['coordinates']['lng'],
            lat=place_data['coordinates']['lat']
        )

        if created:
            for position, image_url in enumerate(place_data['imgs']):
                try:
                    raw_image = requests.get(image_url)
                    content = ContentFile(raw_image.content)
                    instance = PlaceImage.objects.create(place=new_place, position=position)
                    instance.image.save(image_url.split('/')[-1], content, save=True)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'{e}'))
        self.stdout.write(self.style.SUCCESS('Suceccfuly added place'))
