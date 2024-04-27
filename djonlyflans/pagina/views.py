from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

from .models import Flan
from .forms import ContactFormForm
# Create your views here.
def indice(request):
    flanes = Flan.objects.all()
    flanes_pub = Flan.objects.filter(is_private=False)
    flanes_priv = Flan.objects.filter(is_private=True)
    return render (request, 'index.html', {"flanes_pub":flanes_pub})

def acerca(request):
    return render (request, 'about.html', {})

def exito(request):
    return render (request, 'exito.html', {})

def bienvenido(request):
    flanes = Flan.objects.all()
    flanes_pub = Flan.objects.filter(is_private=False)
    flanes_priv = Flan.objects.filter(is_private=True)
    return render (request, 'welcome.html', {"flanes_priv":flanes_priv})


def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/exito")
    else:
        form = ContactFormForm()
    return render(request, "contact.html", {"form": form})


def login_view(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo.'
            return render(request, 'login_view.html', {'error_message': error_message})
    else:
        return render(request, 'login_view.html')

def logout_view(request):
    logout(request)
    return redirect('index')  

class LoginRequiredMixin(TemplateView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class Welcome(LoginRequiredMixin, TemplateView):
    template_name = "welcome.html"