from django.http import HttpResponseNotAllowed, JsonResponse

from core.models import Comentario

import json


# Vista principal para localhost:8000/comentarios
def listar_comentarios(request):
    
    if request.method == "GET":
        comentarios = list(Comentario.objects.values())

        return JsonResponse(comentarios, safe=False, status=200)

    if request.method == "POST":

        # Obtenemos un JSON enviado desde el frontend
        try:
            datos = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "No se proporcionó un JSON válido"}, status=400)

        #Comprobamos que sea un diccionario
        if not isinstance(datos, dict):
            return JsonResponse({"error": "No se ha proporcionado un diccionario válido"}, status=400)

        #Comprobamos que "texto" esté en el diccionario
        if "texto" not in datos:
            return JsonResponse({"error": "Debe proporcionar el campo texto"}, status=400)

        texto = datos["texto"]

        #Comprobamos que el valor de "texto" sea una cadena
        if not isinstance(texto, str):
            return JsonResponse({"error": "El valor de 'texto' no es una cadena"}, status=400)

        texto = texto.strip()

        #Comprobamos que texto no sea una cadena vacía
        if not texto:
            return JsonResponse({"error": "El campo texto es una cadena vacía"}, status=400)

        #Guradamos el comentario en la base de datos
        comentario_nuevo = Comentario.objects.create(
            texto=texto
        )

        #Construimos un diccionario para mandar el comentario
        comentario_nuevo_dict = {
            "id": comentario_nuevo.id,
            "texto": comentario_nuevo.texto
        }

        #Mandamos el comentario nuevo junto con el código de estado 201 (created)
        return JsonResponse(comentario_nuevo_dict, status=201)

    return HttpResponseNotAllowed(["GET"])