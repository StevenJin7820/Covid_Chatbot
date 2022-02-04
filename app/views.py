from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})

def chat(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        context = {}
        context['name'] = username
    return render(request, 'chat.html', context)