from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('register/', views.register, name='register'),  # Contact page
    path('profile/', views.profile, name='profile'),  # Contact page
    path('marketPlace/', views.marketPlace, name='marketPlace'),  # Contact page

    path('', views.marketplace_view, name='marketplace_home'),
    path('product/<int:pk>/', views.product_detail_view, name='product_detail'),
    path('login/', views.login_view, name='login'),
    path('add/', views.add_product_view, name='add_product'),
    path('create-seller-profile/', views.create_seller_profile, name='create_seller_profile'),
    path('browse/', views.browse_products_view, name='browse_products'),

    # Other URL patterns...
    path('checkout/<int:product_id>/', views.checkout_view, name='checkout'),


]
