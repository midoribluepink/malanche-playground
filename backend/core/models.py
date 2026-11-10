from django.db import models

# Modelo de base de datos para los comentarios

class Comentario(models.Model):
    titulo=models.CharField(max_length=100)
    texto=models.TextField(blank=True)

    # Previsualización del objeto Comentario
    def __str__(self):
        return f"{self.titulo[:25]}: {self.texto[:25]}"