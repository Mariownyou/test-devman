from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(upload_to='images/')
    position = models.PositiveIntegerField()
    place = models.ForeignKey(Place, verbose_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.position} {self.place}'  # we could return self.place.title but str(self.place) will already returb this