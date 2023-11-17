from django.shortcuts import render, HttpResponse , get_object_or_404
from django.shortcuts import render
from .forms import InputForm, InputFormVolunteer
from django.shortcuts import render, redirect
from .models import Donate_Money, Volunteer_Work

def home(request):
    return render(request, "home.html")

def gallery(request):
    return render(request, "gallery.html")


def donate(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            obj = Donate_Money(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_number=form.cleaned_data['phone_number'],
                comment=form.cleaned_data['comment'],
                amount=form.cleaned_data['amount'],
                email=form.cleaned_data['email'])
            obj.save()
            return redirect("success_donate")
    else:
        form=InputForm()
    return render(request, "donate.html",{'form': form})

def volunteering(request):

    if request.method == 'POST':
        form = InputFormVolunteer(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            dropdown_selected = form.cleaned_data['Available_Activities']

            existing_instance = Volunteer_Work.objects.get(volun=dropdown_selected)
            existing_instance.first_name = first_name
            existing_instance.last_name = last_name
            existing_instance.phone_number = phone_number
            existing_instance.available='no'
            
            existing_instance.save()  
            return redirect("success_volunteer")
    else:
        form = InputFormVolunteer()

    return render(request, 'volunteering.html', {'form': form})

def celebrate(request):
    return render(request, "celebrate.html")

def success_donate(request):
    return render(request, "success_donate.html")

def success_volunteer(request):
    return render(request, "success_volunteer.html")