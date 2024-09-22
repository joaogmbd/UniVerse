from django.shortcuts import render
from django.contrib.auth import views as auth_views

def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html') 

def produto(request):
    return render(request, 'core/produto.html') 

def registrar(request):
    return render(request, 'core/registrar.html') 

def atletica(request):
    return render(request, 'core/atletica.html') 

def carrinho(request):
    return render(request, 'core/carrinho.html') 