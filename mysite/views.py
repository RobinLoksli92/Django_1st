from json import load
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def show_general(request):
    # template = loader.get_template('index.html')
    # context = {}
    # rendered_page = template.render(context, request)
    # return HttpResponse(rendered_page)
    return render(request, 'index.html')

