from rest_framework.permissions import BasePermission

class IsAuthenticatedOrReadOnly(BasePermission):

       def has_permission(self, request, view):
           # Permite a los usuarios autenticados realizar cualquier acción
           if request.user and request.user.is_authenticated:
               return True
           # Permite a los usuarios no autenticados solo las solicitudes GET
           if request.method in ['GET', 'HEAD', 'OPTIONS']:
               return True
           return False