from app_cursosit.models import Categoria

# Obtengo Todas las Categorias para Usar en el main_navbar

def all_categorias(request):
    categorias = Categoria.objects.all()
    return {'categorias':categorias}

def user_context(request):
    return {'user':request.user}