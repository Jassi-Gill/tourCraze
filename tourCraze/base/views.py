from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import CusUser
from .forms import MyUserCreationForm
from django.http import HttpResponse


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home_page")
        else:
            messages.error(request, "Username or Password does not match!")

    return render(request, "base/login_page.html")


def register_page(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        form.username = request.POST.get("username")
        form.name = request.POST.get("name")
        form.email = request.POST.get("email")
        form.password1 = request.POST.get("password1")
        form.password2 = request.POST.get("password2")

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home_page")
        else:
            messages.error(request, "An Error occured during registration!")
    context = {"form": form}
    return render(request, "base/register_page.html", context)

@login_required(login_url='login_page')
def home_page(request):
    context = {}
    return render(request, "base/home_page.html", context)

@login_required(login_url='login_page')
def community(request, pk):
    context = {pk: pk}
    return render(request, "base/community.html", context)

@login_required(login_url='login_page')
def tours(request, pk):
    context = {pk: pk}
    return render(request, "base/tours.html", context)

@login_required(login_url='login_page')
def update_user(request, pk):
    if(request.user.username != pk):
        redirect(request, "base/home_page.html")
    context = {pk: pk}
    return render(request, "base/tours.html", context)