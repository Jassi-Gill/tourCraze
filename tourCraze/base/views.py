from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "base/Login.html")

def register_page(request):
    return render(request, "base/Login.html")