from django.db import models
from .lote import Lote
from .user import User

class Tostion(models.Model):
    fecha = models.DateTimeField('Fecha',auto_now=False)
    cantidadEntra = models.FloatField('CantidadEntra')
    cantidadSale = models.FloatField('CantidadSale')
    temp1 = models.FloatField('TemperaturaCrack1')
    temp2 = models.FloatField('TemperaturaCrack2')
    temp3 = models.FloatField('TemperaturaCrack3')
    tiempo1 = models.FloatField('TiempoCrack1')
    tiempo2 = models.FloatField('TiempoCrack2')
    tiempo3 = models.FloatField('TiempoCrack3')
    tempPromedio = models.FloatField('TemperaturaPromedio')
    tiempoPromedio = models.FloatField('TiempoPromedio')
    aromas = models.CharField('Aromas', max_length=500)
    tipo = models.CharField('Tipo', max_length=100)
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='Tostion', on_delete=models.CASCADE, blank=True)