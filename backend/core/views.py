from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from core.models import Comentario
from core.serializers import ComentarioModelSerializer


#---- API COMENTARIOS HECHA EN DRF PARA REFRENCIA --------
#---------------------------------------------------------

@ensure_csrf_cookie
def obtener_csrf(request):
    return JsonResponse({"mensaje": "Cookie CSRF configurada"})

# Vista principal para localhost:8000/comentarios
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
