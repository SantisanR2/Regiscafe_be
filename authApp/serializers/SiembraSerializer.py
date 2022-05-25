from rest_framework import serializers
from authApp.serializers.loteSerializer import LoteSerializer
from authApp.models.siembra import Siembra

class SiembraSerializer (serializers.ModelSerializer):
    lote = LoteSerializer()
    class Meta:
        model = Siembra
        fields = ['fecha', 'distancia', 'profundidad', 'inclinacion', 'semilla', 'lote', 'user']