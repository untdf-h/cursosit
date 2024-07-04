from typing import Any
from django.views.generic import View, ListView
from django.shortcuts import render, redirect, get_object_or_404
from app_cursosit.models import *
#from app_cursosit.forms import RegistroForm,LoginForm


class CursoDetalleView(View):
    def get(self,request,id):
        curso = get_object_or_404(Curso,id=id)
        imagen = Imagen.objects.filter(curso=curso).first() # elijo una imagen en el caso que haya muchas.
        return render(request,'detalle.html',{'curso':curso,'imagen':imagen})

# Todos los Cursos de una Categoria
class CategoriaCursosView(View):
    def get(self,request,id):
        categoria_cursos = Curso.objects.filter(categoria=id)
        categoria_id = get_object_or_404(Categoria,id=id)
        return render(request,'categoria_cursos.html',{'categoria_cursos':categoria_cursos,'categoria_id':categoria_id})

    
class BuscadosView(View):
    def get(self,request):
        buscados = Busqueda.busqueda_objects.all() # Manager BusquedaManager
        return render(request, 'index.html',{'buscados':buscados})

class IndexView(View):
    def get(self, request):
        todas_las_categorias = Categoria.objects.all()
        favoritos = Favorito.objects.all()
        buscados = Busqueda.objects.all()

        cursos_por_categoria = {}

        for cat in todas_las_categorias:
            cursos = Curso.objects.filter(categoria=cat)
            cursos_por_categoria [cat] = cursos 

        return render(request,'index.html', {'favoritos':favoritos,
                                             'buscados':buscados,
                                             'cursos_por_categoria':cursos_por_categoria})
    
# class CursosRealizadosView(View):
#     def get(self,request):
#         cursos = UsuarioCurso.objects.filter(usuario = self.pk)
#         return render(request,'perfil_usuario.html',{'cursos':cursos})

# class PerfilProfesorView(View):
#     def get(self,request):
#         profesor = request.user
#         cursos_dictados = Curso.objects.filter(profesor = profesor)
#         return render(request,'perfil_profesor2.html',{'cursos_dictados':cursos_dictados})