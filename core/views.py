from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def quem_somos(request):
    return render(request, 'core/quem_somos.html')


def contato(request):
    return render(request, 'core/contato.html')
