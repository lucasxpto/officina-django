from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContatoForm

from core.models import QuemSomos


def index(request):
    return render(request, 'core/index.html')


def quem_somos(request):
    quem_somos_obj = QuemSomos.objects.first()
    return render(request, 'core/quem_somos.html', {
        'quem_somos': quem_somos_obj
    })


def termos(request):
    return render(request, 'core/termos.html')


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['assunto']
            message = form.cleaned_data['messagem']
            sender = form.cleaned_data['email']
            recipients = ['lucasvital@outlook.com']

            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('header inválido.')
            return HttpResponseRedirect('success')
    else:
        form = ContatoForm()
    return render(request, 'core/contato.html', {
        'form': form
    })


def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.instance.is_staff = True
            form.instance.is_superuser = True
            form.instance.is_active = True
            form.save()

            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'core/registrar.html', {
        'form': form
    })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bem-vindo {username}!")
                return redirect('veiculos:listar')
            else:
                messages.error(request, "Nome de usuário ou senha inválidos.")
        else:
            messages.error(request, "Nome de usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, template_name="core/login.html", context={"form": form})


