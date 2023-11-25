from django.shortcuts import render
from django.shortcuts import render
from .forms import InputForm, InputFormVolunteer, InputFormCelebrations, InputContactInfo
from django.shortcuts import render, redirect
from .models import Donate_Money, Volunteer_Work, Celebrate_Together, Contact_info

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

            existing_instance =Volunteer_Work.objects.get(volun=dropdown_selected)
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
    if request.method == 'POST':
        form = InputFormCelebrations(request.POST)
        if form.is_valid():
            obj = Celebrate_Together(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_number=form.cleaned_data['phone_number'],
                reason=form.cleaned_data['reason'],
                email=form.cleaned_data['email'],
                date_field=form.cleaned_data['date_field'])
            obj.save()
            return redirect("success_celebrate")
    else:
        form=InputFormCelebrations()
    return render(request, "celebrate.html",{'form': form})


def contact(request):
    if request.method == 'POST':
        form = InputContactInfo(request.POST)
        if form.is_valid():
            obj = Contact_info(
                name=form.cleaned_data['name'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'])
            obj.save()
            return redirect("home")
    else:
        form=InputContactInfo()
    return render(request, "contact.html",{'form': form})

def success_donate(request):
    return render(request, "success_donate.html")

def success_volunteer(request):
    return render(request, "success_volunteer.html")

def success_celebrate(request):
    return render(request, "success_celebrate.html")


