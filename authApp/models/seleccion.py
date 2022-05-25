from django.db import models
from .lote import Lote
from .user import User

class Seleccion(models.Model):
    fecha = models.DateTimeField('Fecha',auto_now=False)
    cantidadEntra = models.FloatField('CantidadEntra')
    cantidadSale = models.FloatField('CantidadSale')
    defectuosos = models.FloatField('Defectuosos')
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='Seleccion', on_delete=models.CASCADE, blank=True)