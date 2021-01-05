from django.db import models
from django import forms


class Gallery(models.Model):
    gallery_image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30, primary_key=True)
    image_description = models.TextField()

    class Meta:
        verbose_name_plural = "Gallery"

# class ContactForm(forms.Form):
#     name = models.CharField(max_length=30)
#     email = models.EmailField()
#     message = models.TextField()