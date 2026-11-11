from django.test import TestCase

from core.models import Comentario

class ComentariosTest(TestCase):

    def setUp(self):
        self.comentario1 = Comentario.objects.create(
            texto="Este es el comentario de prueba 1"
        )
        self.comentario2 = Comentario.objects.create(
            texto="Este es el comentario de prueba 2"
        )
        

    def test_listar_comentarios(self):
        url = "/comentarios/"

        respuesta = self.client.get(url)

        datos_respuesta = respuesta.json()

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(len(datos_respuesta), 2)

        comentarios_por_id = {
            comentario["id"]: comentario
            for comentario in datos_respuesta
        }

        self.assertEqual("Este es el comentario de prueba 1", comentarios_por_id[1]["texto"])
        self.assertEqual("Este es el comentario de prueba 2", comentarios_por_id[2]["texto"])