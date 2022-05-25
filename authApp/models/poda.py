from django.db import models
from .lote import Lote
from .user import User

class Poda(models.Model):
    fecha = models.DateTimeField('Fecha', auto_now=False)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='Poda', on_delete=models.CASCADE, blank=True)