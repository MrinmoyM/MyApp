from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'WebApp/home.html')

# Create your views here.

def contact(request):
    return render(request,'WebApp/basic.html'
                  , {'data': ['Please drop me a mail', 'mrinmoy.mimo@yahoo.com']})