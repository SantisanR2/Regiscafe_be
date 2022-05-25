from rest_framework import serializers
from authApp.serializers.loteSerializer import LoteSerializer
from authApp.models.fertilizacion import Fertilizacion

class FertilzacionSerializer (serializers.ModelSerializer):
    lote = LoteSerializer()
    class Meta:
        model = Fertilizacion
        fields = ['relacion', 'fecha', 'lote', 'user']