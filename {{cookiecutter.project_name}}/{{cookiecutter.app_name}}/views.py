from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def home(request: HttpRequest):
    return render(request, "{{cookiecutter.app_name}}/home.html")
