from django.shortcuts import render
from .views import *
import requests

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')