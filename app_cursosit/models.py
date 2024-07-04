from django.db import models, transaction
from django.contrib.auth.models import User,UserManager, AbstractUser


class Categoria (models.Model):
    nombre = models.CharField(max_length= 20,unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return f"{self.nombre}"

class Profesor(models.Model):
    fecha_nacimiento = models.DateField(null=True)
    profesion = models.CharField(max_length=30)
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    titulo = models.CharField(max_length=255, blank=True, null=True)
    experiencia = models.TextField(blank=True, null=True)
    habilidades = models.CharField(max_length=255, blank=True, null=True)
    correo_contacto = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    
    estado = models.CharField(max_length=50, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo'), ('pendiente', 'Pendiente')], default='pendiente')
    disponibilidad = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.user.first_name
    
# Todos los cursos de una Categoria.

class CursoManager(models.Manager):
    def cursos_categoria(self,categoria):
        return self.filter(categoria=categoria)

class Curso (models.Model):
    GRATUITO = 'GR'
    PAGO = 'PA'
    CONDICION_CHOICES = [
        (GRATUITO, 'Gratuito'),
        (PAGO, 'Pago'),
    ]
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    duracion = models.IntegerField()
    cant_leccion = models.IntegerField()
    plan_estudios = models.TextField()
    condicion = models.CharField(max_length=2, choices=CONDICION_CHOICES, default=GRATUITO)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    
    objects = models.Manager()
    categoria_objects = CursoManager()
    
    def __str__(self):
        return self.nombre


class UsuarioCurso(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_realizacion = models.DateTimeField(auto_now_add=True)
    # Otros campos adicionales si es necesario

    def __str__(self):
        return f"{self.usuario.username} - {self.curso.nombre}"


class Modulo (models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

class Leccion (models.Model):
    tema = models.CharField(max_length=40)
    duracion = models.TimeField()
    modulo = models.ForeignKey(Modulo,on_delete=models.CASCADE)


class Pago (models.Model):
    DEBITO = 'DE'
    CREDITO = 'CR'
    FORMA_PAGO_CHOICES = [
        (DEBITO, 'Debito'),
        (CREDITO, 'Credito'),
    ]
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    forma_pago = models.CharField(max_length=2, choices=FORMA_PAGO_CHOICES)
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)


class Favorito (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
   
    objects = models.Manager()
    
    def __str__(self):
        return self.user.username

class Busqueda (models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    
    objects = models.Manager()
   
class Imagen (models.Model):
    arch_imagen = models.ImageField(upload_to="imagenes", null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Video (models.Model):
    arch_video = models.FileField(upload_to='videos/')
    video = models.ForeignKey(Leccion, on_delete=models.CASCADE)



    