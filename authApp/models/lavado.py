from django.db import models
from .lote import Lote
from .user import User

class Lavado(models.Model):
    fechaInicio = models.DateTimeField('FechaInicial',auto_now=False)
    fechaFinal = models.DateTimeField('FechaFinal',auto_now=False)
    cantidadEntra = models.FloatField('CantidadEntra')
    cantidadSale = models.FloatField('CantidadSale')
    cantidadAgua = models.FloatField('CantidadAgua')
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='Lavado', on_delete=models.CASCADE, blank=True)