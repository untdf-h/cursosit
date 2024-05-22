from django.db import models

# Create your models here.


class EstadoCurso(models.Model):
    CONDICIONES_CHOICES = (
        ('PAGO', 'Pago'),
        ('GRATUITO', 'Gratuito'),
    )
    condicion = models.CharField(max_length=10, choices=CONDICIONES_CHOICES)


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()
    condicion = models.ForeignKey("EstadoCurso",on_delete=models.CASCADE)
    plan_estudio = models.CharField(max_length=100)
    duracion = models.IntegerField() # semanas/etc.

class Compra(models.Model):
    total = models.PositiveIntegerField()

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

#class Administrador(user.User)

#class ItemVendido(models.Model):


class Imagen(models.Model):
    nombre = models.CharField(max_length=20)
    imagen = models.ImageField()

class Video(models.Model):
    nombre = models.CharField(max_length=30)
    videopath = models.FileField()
