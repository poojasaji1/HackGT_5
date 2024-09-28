from django.shortcuts import render


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from Leaf.forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    return render(request, 'Leaf/register.html', {'form': form})

def home(request):
    return render(request, 'Leaf/home.html')

def about(request):
    return render(request, 'Leaf/about.html')

def contact(request):
    return render(request, 'Leaf/contact.html')
