from django.shortcuts import render
from django.http import HttpResponse
#from django.http import HttpResponse
#from .crawling import animal

# Create your views here.

def index(request):
    return render(request,'myproject/index.html')