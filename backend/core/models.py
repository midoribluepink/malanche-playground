from django.db import models

# Modelo de base de datos para los comentarios

class Comentario(models.Model):
    texto=models.TextField(blank=True)

    # Previsualización del objeto Comentario
    def __str__(self):
        return f"{self.texto[:25]}"