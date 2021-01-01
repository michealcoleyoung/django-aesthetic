from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Gallery


def home(request):
    return render(request, 'art/index.html', {})


def art(request):
    gallery = Gallery.objects
    return render(request, 'art/art.html', {'gallery': gallery})


def contact(request):
    return render(request, 'art/contact.html', {})


def art_detail(request, pk):
    description = get_object_or_404(Gallery, pk=pk)
    return render(request, 'art/art_detail.html', {'description': description})




