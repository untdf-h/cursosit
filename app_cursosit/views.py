from django.views.generic import View
from django.shortcuts import render
from app_cursosit.models import *

class CursosView(View):
    def get(self,request):
        cursos = Curso.objects.all()
        return render(request,'index.html',{'cursos':cursos})

class FavoritosView(View):
    def get(self,request):
        favoritos = Favorito.objects.all()
        return render(request,'index.html',{'favoritos':favoritos})
    
class BuscadosView(View):
    def get(self,request):
        buscados = Busqueda.objects.all()
        return render(request, 'index.html',{'buscados':buscados})
