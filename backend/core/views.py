from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core.models import Comentario
from core.serializers import ComentarioModelSerializer


#---- API COMENTARIOS HECHA EN DRF PARA REFRENCIA --------
#---------------------------------------------------------

# Función que entrega un token CSRF
@ensure_csrf_cookie
@api_view(["GET"])
def obtener_csrf(request):
    return Response({"mensaje": "Cookie CSRF configurada"})

# Vista principal para localhost:8000/comentarios
@csrf_protect
@api_view(["GET", "POST"])
def listar_comentarios(request):

    if request.method == "GET":
        comentarios = Comentario.objects.all()
        serializer = ComentarioModelSerializer(comentarios, many=True)

        return Response(serializer.data)

    if request.method == "POST":
        serializer = ComentarioModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
