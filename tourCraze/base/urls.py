from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page , name="login_page"), 
    path("register/", views.register_page, name="register_page"),
    path("home/", views.home_page , name="home_page"),
    path("community/<str:pk>", views.community , name="community"),
    path("tours/<str:pk>", views.tours , name="tours"),
]
