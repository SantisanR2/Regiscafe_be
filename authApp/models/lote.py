from django.db import models
from .finca import Finca

class Lote(models.Model):
    cantidad = models.FloatField('Cantidad', blank=True)
    finca = models.ForeignKey(Finca, related_name='Lote', on_delete=models.CASCADE)