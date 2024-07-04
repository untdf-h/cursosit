from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='static/usuarios/img.jpg', upload_to='static/usuarios/')
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=70)

    def __str__(self):
        return self.user.username

def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

def guardar_perfil_usuario(sender, instance, created, **kwargs):
    instance.perfil.save()

post_save.connect(crear_perfil_usuario, sender=User)
post_save.connect(guardar_perfil_usuario, sender=User)
