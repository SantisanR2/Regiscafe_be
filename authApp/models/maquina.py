
from django.db import models
from .despulpado import Despulpado
from .fermentacion import Fermentacion
from .lavado import Lavado
from .molienda import Molienda
from .secado import Secado
from .tostion import Tostion

class Maquina(models.Model):

    #Atributos
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=50)

    #Relaciones
    tostion = models.ForeignKey(Tostion, on_delete=models.CASCADE)
    secado = models.ForeignKey(Secado, on_delete=models.CASCADE)
    molienda = models.ForeignKey(Molienda, on_delete=models.CASCADE)
    fermentacion = models.ForeignKey(Fermentacion, on_delete=models.CASCADE)
    lavado = models.ForeignKey(Lavado, on_delete=models.CASCADE)
    despulpado = models.ForeignKey(Despulpado, on_delete=models.CASCADE)
