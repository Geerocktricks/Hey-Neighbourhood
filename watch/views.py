from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    '''
    view method that displays the home page
    '''
    return render(request , 'index.html')