from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from places.models import Place


def home(request):
    places = Place.objects.all()
    return render(request, 'map/index.html', {'places': places})


def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    images = []
    for image in place.images.order_by('position').all():
        images.append(image.image.url)

    place_data = {
        'title': place.title,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'imgs': images,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }

    return JsonResponse(place_data,
                        content_type='application/json; charset=utf-8',
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})
