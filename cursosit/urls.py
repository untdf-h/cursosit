"""
URL configuration for cursosit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_cursosit.views import * #CursosView, IndexView#, CategoriaView
from app_usuario.views import *
# Para imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('detalle/<int:id>', CursoDetalleView.as_view(), name="curso_detalle"),
    path('categoria/<int:id>', CategoriaCursosView.as_view(), name="categoria_cursos"),
    path('registro/', RegistroView.as_view(), name="registro_usuario"),
    path('login/', LoginView.as_view(), name="login_usuario"),
    path('logout/', logout_view, name="logout_usuario"),
    path('registro_profesor/<int:user_id>', RegistroProfesorView.as_view(), name="registro_profesor"),
    
    path('perfil/', PerfilView.as_view(), name="perfil"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)