from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_page, name="register_page"),
    path("", views.login_page , name="login_page"),
    path("home", views.home_page , name="home_page"),
]
