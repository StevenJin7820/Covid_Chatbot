from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        context = {}
        context['name'] = username
        return render(request, 'chat.html', context)
    return render(request, 'index.html', {})

def chat(request):
    return render(request, 'chat.html')