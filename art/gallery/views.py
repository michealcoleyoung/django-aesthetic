from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Gallery
from django.core.mail import send_mail



def home(request):
    return render(request, 'art/index.html', {})


def art(request):
    gallery = Gallery.objects
    return render(request, 'art/art.html', {'gallery': gallery})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            name,
            email,
            message,
            ['eugene.hilll@ethereal.email'], fail_silently=False,
        )

        return render(request, 'art/contact.html', {})
    else:
        return render(request, 'art/contact.html', {})



def art_detail(request, pk):
    description = get_object_or_404(Gallery, pk=pk)
    return render(request, 'art/art_detail.html', {'description': description})


send_mail('Subject here', 'Here is the message.', 'from@example.com', ['coleyoungmusic@gmail.com'], fail_silently=False)




