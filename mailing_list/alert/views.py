from django.http import HttpResponse
from django.shortcuts import render

def first_view(request):
    if request.method == 'POST':
        return HttpResponse('ok POST')
    else:
        return HttpResponse('ok Get')
