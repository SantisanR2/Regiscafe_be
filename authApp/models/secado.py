from django.db import models
from .lote import Lote
from .user import User

class Secado(models.Model):
    fechaInicio = models.DateTimeField('FechaInicial',auto_now=False)
    fechaFinal = models.DateTimeField('FechaFinal',auto_now=False)
    tempAmb = models.FloatField('TemperaturaAmbiente')
    tempGrano = models.FloatField('TemperaturaGrano')
    humedad = models.FloatField('Humedad')
    densidad = models.FloatField('Densidad')
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='Secado', on_delete=models.CASCADE, blank=True)