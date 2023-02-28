from django.db import models

# Create your models here.
class Game(models.Model):
    #1.-
    juego = models.TextField(default='')
    #2.-
    fecha_de_lanzamiento = models.TextField(default='', blank=False)
    #3.-
    descripcion = models.TextField(default='',)
    #4.-
    tipo = models.TextField(default='')
    #5.-
    creador = models.TextField(default='')
    #6.-
    personajes = models.TextField(default='')
    #7.-
    enemigos = models.TextField(default='')
    #8.-
    precio = models.DecimalField(default=0, max_digits=20, decimal_places=2, blank=False)
    #9.-
    musica = models.TextField(default='')
    #10
    version = models.TextField(default='')
    
    