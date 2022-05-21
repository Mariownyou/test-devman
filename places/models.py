from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description_short = models.TextField(blank=True, null=False, verbose_name='Короткое описание')
    description_long = HTMLField(blank=True, null=False, verbose_name='Описание')
    lng = models.DecimalField(max_digits=17, decimal_places=14, verbose_name='Долгота')
    lat = models.DecimalField(max_digits=17, decimal_places=14, verbose_name='Широта')
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name='Картинка')
    position = models.PositiveIntegerField(default=0)
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE, verbose_name='Место')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place}'
