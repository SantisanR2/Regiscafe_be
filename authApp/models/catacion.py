from django.db import models
from .lote import Lote
from .user import User

class Catacion(models.Model):
    fecha = models.DateTimeField('Fecha',auto_now=False)
    tiempo1 = models.FloatField('Tiempo1')
    tiempo2 = models.FloatField('Tiempo2')
    tiempo3 = models.FloatField('Tiempo3')
    puntaje = models.FloatField('Puntaje')
    lote = models.OneToOneField(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='CAtacion', on_delete=models.CASCADE, blank=True)