from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def gallery(request):
    return render(request, "gallery.html")


def donate(request):
    return render(request, "donate.html")

def volunteering(request):
    return render(request, "volunteering.html")

def celebrate(request):
    return render(request, "celebrate.html")