from django.shortcuts import render, redirect

from apps.persons import urls
from .models import *
from .forms import *

# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return render(request, 'main.html', {})
    return redirect('login')

def chequesTerceros(request):
    if request.user.is_authenticated:
        return render(request, 'third.html', {})
    return redirect('login')

def bancos(request):
    if request.user.is_authenticated:

        bancos = Banco.objects.all()

        form = BancoForm()
        if request.method == "POST":
            form = BancoForm(request.POST)

            if form.is_valid():
                instancia = form.save(commit=False)
                instancia.save()
                return redirect('bancos')
        return render(request, 'banks.html', {'form': form, 'bancos': bancos})
    return redirect('login')

def cuentas(request):
    if request.user.is_authenticated:

        form = CuentasCorrienteForm()
        if request.method == "POST":
            form = CuentasCorriente(request.POST)

            if form.is_valid():
                instacia = form.save(commit=False)
                instancia.save()
                return redirect('cuentas')
        return render(request, 'accounts.html', {'form': form})
    return redirect('login')

def chequesPropios(request):
    if request.user.is_authenticated:
        
        form = ChequePropioForm()
        if request.method == "POST":
            form = ChequePropioForm(request.POST)

            if form.is_valid():
                instancia = form.save(commit=False)
                instancia.save()
                return redirect('cheques-propios')
        return render(request, 'own.html', {'form': form})
    return redirect('login')