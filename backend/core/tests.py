from django.test import TestCase

from core.models import Comentario

# Clase de preubas
class ComentariosTest(TestCase):

    #Datos de prueba de la base de datos
    def setUp(self):
        self.comentario1 = Comentario.objects.create(
            texto="Este es el comentario de prueba 1"
        )
        self.comentario2 = Comentario.objects.create(
            texto="Este es el comentario de prueba 2"
        )
        
    # Prueba de la vista localhost:8000/comentarios con el método GET
    def test_listar_comentarios_get(self):
        url = "/comentarios/"

        #Construimos la petición GET
        respuesta = self.client.get(url)
        datos_respuesta = respuesta.json()

        #Comprobamos el código de estado correcto y la cantidad de objetos recibidos
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(len(datos_respuesta), 2)

        #Ordenamos los objetos por "id"
        comentarios_por_id = {
            comentario["id"]: comentario
            for comentario in datos_respuesta
        }

        #Comprobamos que los elemenos recibidos son los que hay en nuestra base de datos
        self.assertEqual("Este es el comentario de prueba 1", comentarios_por_id[1]["texto"])
        self.assertEqual("Este es el comentario de prueba 2", comentarios_por_id[2]["texto"])


    #Prueba de la vista localhost:8000/comentarios con el método POST
    def test_listar_comentarios_post_valido(self):

        #Construimos el comentario de prueba
        nuevo_comentario = {
            "texto": "Comentario de prueba"
        }

        #Construimos la petición POST
        respuesta = self.client.post(
            "/comentarios/",
            data=nuevo_comentario,
            content_type="application/json"
        )

        datos_respuesta = respuesta.json()

        #Validaciones

        #Código de estado 201 CREATED
        self.assertEqual(respuesta.status_code, 201)

        #"texto" se encuentra en la respuesta del servidor
        self.assertIn("texto", datos_respuesta) 

        #"texto" corresponde al comentario de prueba
        self.assertEqual("Comentario de prueba", datos_respuesta["texto"])

        #El comentario de prueba se creó en la base de datos
        self.assertTrue(Comentario.objects.filter(id=datos_respuesta["id"]).exists())

    def test_listar_comentarios_post_invalido(self):

        #Casos donde el comentario no está bien hecho
        casos = [
            {}, #Diccionario vacío
            '{"texto"}', #JSON mal formado
            {"texto": 2343}, #texto no es una cadenda
            {"texto": ""}, #texto contiene una cadena vacía
            12345, #No es un diccionario
            {"otro_campo": "Hola"} #El diccionario no contiene los campos correctos
        ]

        #Cada caso será evaluado por separado
        for caso in casos:
            with self.subTest(caso=caso):

                #Número actual de elementos en la base de datos
                num_base_datos = Comentario.objects.count()

                #Construimos la petición POST
                respuesta = self.client.post(
                    "/comentarios/",
                    data=caso,
                    content_type="application/json"
                )

                datos_respuesta = respuesta.json()

                #Validaciones

                #Código de error 400 BAD REQUEST
                self.assertEqual(respuesta.status_code, 400)

                #La respuesta contiene un mensaje de error
                self.assertIn("error", datos_respuesta)

                #La cantidad de objetos en la base de datos no sufrió cambios
                self.assertEqual(num_base_datos, Comentario.objects.count())
