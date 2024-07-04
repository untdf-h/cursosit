from django.contrib.auth.models import Group

from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Perfil

@receiver(post_save, sender=Perfil)
def agregar_user_a_grupo_alumno(sender, instance, created, **kwargs):
    if created:
        try:
            alumnos = Group.objects.get(name='alumno')
        except Group.DoesNotExist:
            alumnos = Group.objects.create(name='alumno')
            alumnos = Group.objects.create(name='profesor')
        instance.user.groups.add(alumnos)