from django.shortcuts import render, get_object_or_404
from places.models import Place, Image
from django.http import JsonResponse
from django.urls import reverse


def show_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = Image.objects.filter(place=place)
    place_details = {
        'title': place.name,
        'imgs': [
          image.image.url for image in images
        ],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.long,
            'lat': place.lat
        }
    }
    return JsonResponse(
      place_details, 
      json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )


def show_general(request):
    features = []
    context = {'places': {
      'type': 'FeatureCollection',
      'features': features
    }}

    for place in Place.objects.all():

        feature = {
          'type': 'Feature',
          'geometry': {
            'type': 'Point',
            'coordinates': [place.long, place.lat]
          },
          'properties': {
            'title': place.name,
            'placeId': place.name,
            'detailsUrl': reverse(show_place, args=[place.id])
          }
        }
        features.append(feature)
    return render(request, 'index.html', context)
