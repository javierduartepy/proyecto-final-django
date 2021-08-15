from functools import update_wrapper
from django.db import models

# Create your models here.
class Quiz(models.Model):
    pregunta = models.TextField() #TextField nos permite escribir grandes textos
    respuesta = models.CharField(max_length = 50) #CharField nos permite escribir pero con un limite que ntros debemos marcar
    opcion1 = models.TextField()
    opcion2 = models.TextField()
    opcion3 = models.TextField()
    opcion4 = models.TextField()
    categoria = models.CharField(max_length = 100)
    imagen = models.URLField(null = True, blank = True, verbose_name = 'Link de la imagen')
    created = models.DateTimeField(auto_now_add = True, verbose_name= 'Fecha de Creación')
    updated = models.DateTimeField(auto_now = True, verbose_name= 'Fecha de Edición')
    

    class Meta:
        db_table = 'quiz'
        verbose_name = 'cuestionario'
        ordering = ['categoria']

    def __str__(self) -> str:
        return self.pregunta    
