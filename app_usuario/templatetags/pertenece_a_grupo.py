# Importa los módulos necesarios
from django import template
from django.contrib.auth.models import Group

# Registra tu biblioteca de etiquetas
register = template.Library()

# Define la función de etiqueta
@register.filter(name='pertenece_a_grupo')
def pertenece_a_grupo(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
        return group in user.groups.all()
    except Group.DoesNotExist:
        return False
