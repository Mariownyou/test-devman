from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render

from places.models import Place


def get_home_page(request):
    places = Place.objects.all()
    return render(request, 'map/index.html', {'places': places})


def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    links = []
    images = place.images.order_by('position').all()
    [links.append(image.image.url) for image in images]

    place_serialized = {
        'title': place.title,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'imgs': links,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }

    return JsonResponse(place_serialized,
                        content_type='application/json; charset=utf-8',
                        json_dumps_params={'ensure_ascii': False, 'indent': 2})
