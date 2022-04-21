from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template


def home(request):
    # map_template = get_template('map/index.html')
    return render(request, 'map/index.html', {})
