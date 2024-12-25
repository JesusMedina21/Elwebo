from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import random
from .permissions import IsAuthenticatedOrReadOnly  # Asegúrate de importar tu clase de permisos


#El modelo es la base de datos, aqui cree un validador para escribir solo numeros 

def validate_only_letters_and_spaces(value):
    if not value.replace(" ", "").isalpha():
        raise ValidationError(
            _('El campo título de la materia solo puede contener letras y espacios.'),
            code='invalid'
        )
#Esta es la tabla con los campos

class Instrumento(models.Model):
    Nombre_Del_Instrumento = models.CharField(max_length=100,  unique=True, validators=[validate_only_letters_and_spaces])
    Familia_Del_Instrumento = models.CharField(max_length=50)
    Foto = models.CharField(max_length=1000,  unique=True)
