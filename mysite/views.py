from django.shortcuts import render, get_object_or_404
from places.models import Place, Image
from django.http import JsonResponse


def show_place(request, id):
    place = get_object_or_404(Place, id=id)
    images = Image.objects.filter(place=place)
    response_data = {
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
      response_data, 
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
            'detailsUrl': f'places/{place.id}'
          }
        }
        features.append(feature)
        return render(request, 'index.html', context)
