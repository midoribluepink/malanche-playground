from rest_framework import serializers
from core.models import Cliente, Comentario

class ClientModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nombre", "apellidos", "telefono", "fecha_registro"] 
        read_only_fields = ["id", "fecha_registro"]




#---- SERIALIZER PARA EL MODEL COMENTARIO (API ANTIGUA)---
#---------------------------------------------------------
class ComentarioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ["texto"]