from django.db import models
from .lote import Lote
from .user import User

class Molienda(models.Model):
    fecha = models.DateTimeField('Fecha', auto_now=False)
    cantidadEntra = models.FloatField('CantidadEntra')
    cantidadSale = models.FloatField('CantidadSale')
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='Molienda', on_delete=models.CASCADE, blank=True)