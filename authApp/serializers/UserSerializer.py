from rest_framework import serializers
from authApp.models.user import User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'password', 'correo', 'finca', 'is_recolector', 'is_admin', 'cedula', 'celular', 'fecha']
        
