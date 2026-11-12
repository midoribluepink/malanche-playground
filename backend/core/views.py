from django.http import HttpResponseNotAllowed, JsonResponse

from core.models import Comentario

def listar_comentarios(request):

    if request.method == "GET":
        comentarios = list(Comentario.objects.values())

        return JsonResponse(comentarios, safe=False, status=200)

    return HttpResponseNotAllowed(["GET"])