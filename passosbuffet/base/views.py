from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def servico(request):
    return render(request, 'servicos.html')

def contato(request):
    return render(request, 'contato.html')