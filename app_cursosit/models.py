from django.db import models


class Imagen (models.Model):
    arch_imagen = models.FileField(upload_to='imagenes/')

class Video (models.Model):
    arch_video = models.FileField(upload_to='videos/')

class Pago (models.Model):
    DEBITO = 'DE'
    CREDITO = 'CR'
    FORMA_PAGO_CHOICES = [
        (DEBITO, 'Debito'),
        (CREDITO, 'Credito'),
    ]
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    forma_pago = models.CharField(max_length=2, choices=FORMA_PAGO_CHOICES)

class Leccion (models.Model):
    tema = models.CharField(max_length=40)
    duracion = models.TimeField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Modulo (models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    leccion = models.ForeignKey(Leccion,on_delete=models.CASCADE)

class Curso (models.Model):
    GRATUITO = 'GR'
    PAGO = 'PA'
    CONDICION_CHOICES = [
        (GRATUITO, 'Gratuito'),
        (PAGO, 'Pago'),
    ]
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)
    duracion = models.IntegerField()
    cant_leccion = models.IntegerField()
    plan_estudios = models.CharField(max_length=100)
    condicion = models.CharField(max_length=2, choices=CONDICION_CHOICES, default=GRATUITO)
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE)

class Alumno (models.Model):
    nombre = models.CharField(max_length=30)
    dni = models.BigIntegerField
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)

class Profesor (models.Model):
    legajo = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

