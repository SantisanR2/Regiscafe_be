from rest_framework import serializers
from authApp.serializers.loteSerializer import LoteSerializer
from authApp.models.poda import Poda

class PodaSerializer (serializers.ModelSerializer):
    lote = LoteSerializer()
    class Meta:
        model = Poda
        fields = ['fecha', 'lote', 'user']