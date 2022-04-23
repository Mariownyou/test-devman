from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

from places.models import Place


def home(request):
    # map_template = get_template('map/index.html')
    places = Place.objects.all()
    return render(request, 'map/index.html', {'places': places})
