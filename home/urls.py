from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('menu', views.menu, name="menu"),
    path('directions', views.directions, name="directions"),
    path('pricing', views.pricing, name="pricing"),
    path('login', views.login, name="login"),
    path('registration', views.registration, name="registration"),
    path('feedback', views.feedback, name="feedback")
    ]
