from rest_framework import serializers
from authApp.serializers.loteSerializer import LoteSerializer
from authApp.models.riego import Riego

class RiegoSerializer (serializers.ModelSerializer):
    lote = LoteSerializer()
    class Meta:
        model = Riego
        fields = ['fecha', 'agua', 'lote', 'user']