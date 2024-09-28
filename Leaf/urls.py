from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('register/', views.register, name='register'),  # Contact page
path('profile/', views.profile, name='profile'),  # Contact page
path('marketPlace/', views.marketPlace, name='marketPlace'),  # Contact page

]
