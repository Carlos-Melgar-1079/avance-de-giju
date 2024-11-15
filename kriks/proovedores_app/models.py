from django.db import models

# Create your models here.

class proovedores(models.Model):
    codigo=models.CharField( primary_key=True, max_length=50)
    nombre=models.CharField( max_length=50)
    telefono=models.CharField( max_length=50)
    edad=models.CharField( max_length=50)
    ine=models.CharField( max_length=50)
    permiso=models.CharField( max_length=50)
    matricula=models.CharField( max_length=50)

    def __str__(self):
        return self. nombre