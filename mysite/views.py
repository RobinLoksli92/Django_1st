import json
from json import load
from django.shortcuts import render
from places.models import Place


def show_general(request):
  features = []
  context = {'places': {
      "type": "FeatureCollection",
      "features": features
  }}

  for place in Place.objects.all():
    
    feature = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.long, place.lat]
          },
          "properties": {
            "title": place.name,
            "placeId": place.name,
            "detailsUrl": "static/places/moscow_legends.json"
          }
        }
    features.append(feature)
  return render(request, 'index.html', context)

