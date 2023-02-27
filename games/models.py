from django.db import models
from django.conf import settings
from django.utils.timezone import now

# Create your models here.
class game(models.Model):
    #1.-
    juego = models.TextField(default='Apex legends', blank=False)
    #2.-
    fecha_de_lanzamiento = models.TextField(default='', blank=False)
    #3.-
    descripcion = models.TextField(default='una batalla por trios o duos', blank=False)
    #4.-
    tipo = models.TextField(default='de disparos', blank=False)
    #5.-
    creador = models.TextField(default='chino', blank=False)
    #6.-
    personajes = models.TextField(default='lifeline, octane, wraith, ect', blank=False)
    #7.-
    enemigos = models.TextField(default='equipo contrario', blank=False)
    #8.-
    precio = models.DecimalField(default=0, max_digits=20, decimal_places=2, blank=False)
    #9.-
    musica = models.TextField(default='12', blank=False)
    #10
    version = models.TextField(default='12', blank=False)
    
    