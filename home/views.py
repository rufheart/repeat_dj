from django.shortcuts import render
from requests import request

def home(request):
    return render(request, 'home.html')
