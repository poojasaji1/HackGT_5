from django.shortcuts import render

def home(request):
    return render(request, 'Leaf/home.html')

def about(request):
    return render(request, 'Leaf/about.html')

def contact(request):
    return render(request, 'Leaf/contact.html')

def register(request):
    return render(request, 'Leaf/register.html')
