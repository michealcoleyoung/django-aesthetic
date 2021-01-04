from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Gallery, ContactForm
from django.core.mail import send_mail, BadHeaderError



def home(request):
    return render(request, 'art/index.html', {})


def art(request):
    gallery = Gallery.objects
    return render(request, 'art/art.html', {'gallery': gallery})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['eugene.hilll@ethereal.email'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'art/contact.html', {'form': form})


def art_detail(request, pk):
    description = get_object_or_404(Gallery, pk=pk)
    return render(request, 'art/art_detail.html', {'description': description})


send_mail('Subject here', 'Here is the message.', 'from@example.com', ['coleyoungmusic@gmail.com'], fail_silently=False)




