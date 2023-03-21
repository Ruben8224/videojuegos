from django.db import models


# Create your models here.
class Game(models.Model):
    #1.-
    juego = models.TextField(default='Apex')
    #2.-
    fecha_de_lanzamiento = models.TextField(default='###', blank=False)
    #3.-
    descripcion = models.TextField(default='Tiros',)
    #4.-
    tipo = models.TextField(default='Rpg')
    #5.-
    creador = models.TextField(default='chinito')
    #6.-
    personajes = models.TextField(default='el sin patas')
    #7.-
    enemigos = models.TextField(default='La pelona')
    #8.-
    precio = models.DecimalField(default=0, max_digits=20, decimal_places=2, blank=False)
    #9.-
    musica = models.TextField(default='un millon de primaveras')
    #10
    version = models.TextField(default='')
    
    