from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from .forms import LoginForm, RegistroForm, RegistroProfesorForm

from django.contrib.auth.models import User
##
from django.contrib.auth.models import Group
# Prueba generic
from django.views.generic.edit import CreateView
from app_cursosit.models import Curso, UsuarioCurso, Profesor
####
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


import logging

logger = logging.getLogger(__name__)



@method_decorator(login_required(login_url='login_usuario'), name='dispatch')
class RegistroProfesorView(View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)

        if hasattr(user,'profesor'):
            return redirect('perfil')
        form = RegistroProfesorForm()
        return render(request, 'registro_profesor.html', {'form': form, 'user': user})

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        form = RegistroProfesorForm(request.POST)
        
        if form.is_valid():
            profesor = form.save(commit=False)
            profesor.user = user
            profesor.save()
            
            # Cambiar grupo de 'Alumno' a 'Profesor'
            alumno_group = Group.objects.get(name='alumno')
            profesor_group = Group.objects.get(name='profesor')
            user.groups.remove(alumno_group)
            user.groups.add(profesor_group)
            
            return redirect('perfil')
        
        return render(request, 'registro_profesor.html', {'form': form, 'user': user})


class RegistroView(View):
    def get(self, request):
        form = RegistroForm()
        return render(request, 'registro.html', {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('perfil')
        return render(request, 'registro.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('perfil')
            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrectos")
        return render(request, 'login.html', {'form': form})


@method_decorator(login_required(login_url='login_usuario'), name='dispatch')
class PerfilView(View):
    def get(self, request):
        usuario = request.user
        
        
        if Group.objects.get(name='profesor') in usuario.groups.all():
            profesor = Profesor.objects.get(user=usuario)
            cursos_dicta = Curso.objects.filter(profesor=profesor)    #ver
            return render(request, 'perfil_profesor.html', {'cursos': cursos_dicta, 'usuario': usuario})
        else:
            cursos_hace = UsuarioCurso.objects.filter(user=usuario)            #ver
            return render(request, 'perfil_usuario.html', {'cursos': cursos_hace, 'usuario': usuario})
        


def logout_view(request):
    logout(request)
    return redirect('index')
