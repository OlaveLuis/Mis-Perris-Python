from django.db import models

# Create your models here.

class Perro(models.Model):
	codigo = models.CharField(max_length=10)
	nombre = models.CharField(max_length=50)
	tamaño = models.PositiveIntegerField()
	peso = models.PositiveIntegerField()
	color = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100)
	op = (('A','Activo'),('I','Inactivo'))
	estado = models.CharField(max_length=1, choices=op, default='A')

	def __str__(self):
		return "{0} {1}".format(self.codigo, self.nombre)
