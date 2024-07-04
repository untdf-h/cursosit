import json
from faker import Faker
from random import randint, choice
from datetime import datetime, timedelta

fake = Faker()

fixture = []

# Generate Categorias
for i in range(1, 6):
    fixture.append({
        "model": "app_cursosit.categoria",
        "pk": i,
        "fields": {
            "nombre": fake.word(),
            "fecha_creacion": fake.date_time_this_decade().isoformat(),
            "descripcion": fake.text()
        }
    })


# Generate Profesores
for i in range(1, 6):
    fixture.append({
        "model": "app_cursosit.profesor",
        "pk": i,
        "fields": {
            "fecha_nacimiento": fake.date_of_birth(minimum_age=25, maximum_age=60).isoformat(),
            "profesion": fake.job(),
            "user": i,
            "titulo": fake.sentence(nb_words=5),
            "experiencia": fake.text(),
            "habilidades": ', '.join(fake.words(nb=5)),
            "correo_contacto": fake.email(),
            "telefono": fake.phone_number(),
            "estado": choice(['activo', 'inactivo', 'pendiente']),
            "disponibilidad": fake.sentence(nb_words=5)
        }
    })

# Generate Cursos
for i in range(1, 11):
    fixture.append({
        "model": "app_cursosit.curso",
        "pk": i,
        "fields": {
            "nombre": fake.word(),
            "descripcion": fake.text(),
            "duracion": randint(10, 100),
            "cant_leccion": randint(1, 20),
            "plan_estudios": fake.text(),
            "condicion": choice(['GR', 'PA']),
            "categoria": randint(1, 5),
            "precio": round(fake.random_number(digits=3), 2),
            "profesor": randint(1, 5)
        }
    })

# Generate UsuarioCurso
for i in range(1, 11):
    fixture.append({
        "model": "app_cursosit.usuariocurso",
        "pk": i,
        "fields": {
            "user": randint(1, 10),
            "curso": randint(1, 10),
            "fecha_realizacion": fake.date_time_this_year().isoformat()
        }
    })

# Generate Modulos
for i in range(1, 11):
    fixture.append({
        "model": "app_cursosit.modulo",
        "pk": i,
        "fields": {
            "nombre": fake.word(),
            "cantidad": randint(1, 10),
            "curso": randint(1, 10)
        }
    })

# Generate Lecciones
for i in range(1, 11):
    fixture.append({
        "model": "app_cursosit.leccion",
        "pk": i,
        "fields": {
            "tema": fake.sentence(nb_words=3),
            "duracion": (datetime.min + timedelta(minutes=randint(5, 90))).time().isoformat(),
            "modulo": randint(1, 10)
        }
    })

# Generate Pagos
for i in range(1, 6):
    fixture.append({
        "model": "app_cursosit.pago",
        "pk": i,
        "fields": {
            "monto": round(fake.random_number(digits=3), 2),
            "fecha": fake.date_time_this_year().isoformat(),
            "forma_pago": choice(['DE', 'CR']),
            "alumno": randint(1, 10)
        }
    })

# Generate Favoritos
for i in range(1, 6):
    fixture.append({
        "model": "app_cursosit.favorito",
        "pk": i,
        "fields": {
            "user": randint(1, 10),
            "curso": randint(1, 10),
            "fecha": fake.date_time_this_year().isoformat()
        }
    })

# Generate Busquedas
for i in range(1, 6):
    fixture.append({
        "model": "app_cursosit.busqueda",
        "pk": i,
        "fields": {
            "curso": randint(1, 10),
            "fecha": fake.date_time_this_year().isoformat()
        }
    })

# Generate Imagenes
for i in range(1, 6):
    fixture.append({
        "model": "app_cursosit.imagen",
        "pk": i,
        "fields": {
            "arch_imagen": fake.file_name(extension='jpg'),
            "curso": randint(1, 10)
        }
    })

# Generate Videos
for i in range(1, 6):
    fixture.append({
        "model": "app_cursosit.video",
        "pk": i,
        "fields": {
            "arch_video": fake.file_name(extension='mp4'),
            "video": randint(1, 10)
        }
    })

# Write the fixture to a file
with open('fixture.json', 'w') as f:
    json.dump(fixture, f, indent=2)
