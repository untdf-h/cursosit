from django.contrib import admin
from app_cursosit.models import *

# Register your models here.

admin.site.register(Curso)

admin.site.register(Categoria)
admin.site.register(Pago)
admin.site.register(Modulo)
admin.site.register(Leccion)
admin.site.register(Favorito)
admin.site.register(Busqueda)

admin.site.register(UsuarioCurso)
admin.site.register(Profesor)

admin.site.register(Imagen)


