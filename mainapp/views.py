from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def demand(request):
    return render(request, 'demand.html')

def geography(request):
    return render(request, 'geography.html')