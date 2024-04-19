from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Feedback, Registration, Menu
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def menu(request):
    return render(request, 'menu.html')

def directions(request):
    return render(request, 'directions.html')

def pricing(request):
    return render(request, 'pricing.html')

def myaccount(request):
    return render(request, 'login.html')

def registration(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        registration = Registration(name=name, email=email, phone=phone, date=datetime.today())
        registration.save()
        messages.success(request, 'Your message has been sent..!')

    return render(request, 'registration.html')

def feedback(request):
    if request.method == "POST":
        name= request.POST.get('name')
        user_feedback =request.POST.get('user_')
        feedback = Feedback(name=name, user_feedback=user_feedback)
        feedback.save()
        messages.success(request, 'Thank you for your response..!')

    return render(request, 'feedback.html')


