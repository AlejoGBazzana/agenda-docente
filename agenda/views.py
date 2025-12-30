from django.shortcuts import render
from .models import PerfilUsuario
from .models import Colegio

def inicio(request):
    docente = PerfilUsuario.objects.first()
    return render(request, 'agenda/inicio.html', {'docente': docente})

def listado_colegios(request):
    colegios = Colegio.objects.all()
    return render(request, 'listado_colegios.html', {'colegios': colegios})