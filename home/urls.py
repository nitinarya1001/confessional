from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="homePage"),
    path('confess', views.confess, name="confessPage"),
    path('confession', views.confession, name="confessionPage"),
    path('aboutus', views.aboutus, name="aboutPage"),
    path('contactus', views.contactus, name="contactPage"),
]
