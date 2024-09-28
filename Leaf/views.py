
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from Leaf.forms import CustomUserCreationForm
from .models import Product


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Leaf/register.html', {'form': form})

def home(request):
    return render(request, 'Leaf/home.html')
def profile(request):
    return render(request, 'Leaf/profile.html')
def marketPlace(request):
    return render(request, 'Leaf/marketPlace.html')

def about(request):
    return render(request, 'Leaf/about.html')

def contact(request):
    return render(request, 'Leaf/contact.html')

def marketplace_view(request):
    products = Product.objects.filter(available=True)
    return render(request, 'Leaf/markethome.html', {'products': products})


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'Leaf/product_detail.html', {'product': product})

from django.shortcuts import redirect
from .forms import ProductForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Seller, Product
@login_required(login_url='login')
def add_product_view(request):
    try:
        seller = Seller.objects.get(user=request.user)
    except Seller.DoesNotExist:
        # Redirect to seller profile creation page or show an error message
        return redirect('create_seller_profile')  # Replace with your actual URL name

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user.seller
            product.save()
            return redirect('marketplace_home')

    else:
        form = ProductForm()
    return render(request, 'Leaf/add_product.html', {'form': form})



from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('home')

                # go to settings.py to change redirect behavior after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'Leaf/login.html', {'form': form})

from django.shortcuts import render, redirect
from .models import Seller
from .forms import SellerForm  # Assuming you have a SellerForm

@login_required
def create_seller_profile(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user
            seller.save()
            return redirect('add_product')  # Redirect to the add product page
    else:
        form = SellerForm()

    return render(request, 'Leaf/create_seller_profile.html', {'form': form})
