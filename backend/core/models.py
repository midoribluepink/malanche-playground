from django.db import models

# Modelo de base de datos para los clientes
class Cliente(models.Model):
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=150)
    telefono=models.CharField(max_length=20, blank=True)
    fecha_registro=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

# Modelo de base de datos para los comentarios

class Comentario(models.Model):
    texto=models.TextField(blank=True)

    # Previsualización del objeto Comentario
    def __str__(self):
        return f"{self.texto[:25]}"