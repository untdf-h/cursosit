import requests
from django.utils.timezone import now
from app_cursosit.models import Categoria, Curso

import sys
import os

# Añadir el directorio del proyecto al sys.path
sys.path.append(os.path.abspath('ruta/a/tu/proyecto'))

# Importar los modelos
#from m.models import Categoria, Curso

def importar_categorias_y_cursos():
    url_categorias = 'https://api.coursera.org/api/courses.v1/categories'
    response_categorias = requests.get(url_categorias)
    if response_categorias.status_code == 200:
        categorias_data = response_categorias.json()['elements']
        for categoria_data in categorias_data:
            nombre = categoria_data.get('name', '')
            descripcion = categoria_data.get('description', '')
            # Crear o actualizar categoría
            categoria, created = Categoria.objects.update_or_create(
                nombre=nombre,
                defaults={'descripcion': descripcion, 'fecha_creacion': now()}
            )

            # Obtener cursos de la categoría
            url_cursos = f'https://api.coursera.org/api/courses.v1/courses?fields=slug,name,photoUrl&q=category:{categoria_data["id"]}'
            response_cursos = requests.get(url_cursos)
            if response_cursos.status_code == 200:
                cursos_data = response_cursos.json()['elements']
                for curso_data in cursos_data:
                    nombre_curso = curso_data.get('name', '')
                    descripcion_curso = curso_data.get('description', '')
                    # Crear curso
                    Curso.objects.create(
                        nombre=nombre_curso,
                        descripcion=descripcion_curso,
                        duracion=curso_data.get('duration', 0),
                        cant_leccion=curso_data.get('lesson_count', 0),
                        plan_estudios=curso_data.get('syllabus', ''),
                        condicion=Curso.GRATUITO if curso_data.get('is_paid', False) else Curso.PAGO,
                        categoria=categoria,
                        precio=float(curso_data.get('price', 0)),
                        profesor=None  # Aquí debes asignar el profesor adecuado
                    )
            else:
                print(f'Error al obtener cursos para la categoría {nombre}: {response_cursos.status_code}')
    else:
        print(f'Error al obtener categorías: {response_categorias.status_code}')

def main():
    importar_categorias_y_cursos()

if __name__ == '__main__':
    main()
