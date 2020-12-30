from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('art/', views.art, name='art'),
    path('contact/', views.contact, name='contact'),
    path('art/<int:pk>/', views.art_detail, name='art_detail'),
]


