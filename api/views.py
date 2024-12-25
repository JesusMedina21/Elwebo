from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Instrumento
from .serializer import InstrumentoSerializer
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from rest_framework.permissions import BasePermission
from .permissions import IsAuthenticatedOrReadOnly 
from django.contrib.auth import login, logout as auth_logout, authenticate  

# Esta clase es para que la API convierta el codigo a JSON.
class InstrumentoViewSet(viewsets.ModelViewSet):
    queryset = Instrumento.objects.all()
    serializer_class = InstrumentoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    
#Pagina de inicio 
def inicio(request):
    return render(request, 'home.html')

def documentacion(request):
    return render(request, 'documentacion.html')



def error(request):
    return render(request, '404.html')


def mantenimiento(request):
    return render(request, '400.html')


def logout_view(request): 
    auth_logout(request) 
    return redirect('inicio')
