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
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f'Could not load file\n{response.text}'))
            return
        raw_place = response.json()
        place, created = Place.objects.update_or_create(
            title=raw_place['title'],
            defaults=dict(
                description_short=raw_place['description_short'],
                description_long=raw_place['description_long'],
                lng=raw_place['coordinates']['lng'],
                lat=raw_place['coordinates']['lat']
            )
        )

        if not created:
            self.stdout.write(self.style.SUCCESS('Suceccfuly added place'))
            return
        for position, image_url in enumerate(raw_place['imgs']):
            try:
                raw_image = requests.get(image_url)
                if raw_image.status_code != 200:
                    self.stdout.write(self.style.ERROR(f'Could not load image\n{raw_image.text}'))
                    return
                content = ContentFile(raw_image.content)
                instance = PlaceImage.objects.create(place=place, position=position)
                instance.image.save(image_url.split('/')[-1], content, save=True)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'{e}'))
        self.stdout.write(self.style.SUCCESS('Suceccfuly added place'))
