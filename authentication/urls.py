from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('BuyNow',views.BuyNow, name="BuyNow"),
    path('Rent', views.Rent, name="Rent"),
    path('index', views.index, name="index"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('Logout', views.Logout, name="Logout"),

]