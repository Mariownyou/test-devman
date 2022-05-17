from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField(blank=True, null=True)
    description_long = HTMLField(blank=True, null=True)
    lng = models.DecimalField(max_digits=17, decimal_places=14)
    lat = models.DecimalField(max_digits=17, decimal_places=14)
    position = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(upload_to='images/')
    position = models.PositiveIntegerField(default=0)
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place}'
