from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})

def chat(request):        
    return render(request, 'chat.html')