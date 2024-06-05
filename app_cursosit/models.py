from django.db import models
from django.contrib.auth.models import User,UserManager, AbstractUser


class Alumno (models.Model):
    alumno = models.OneToOneField(User,on_delete=models.CASCADE,blank=False,null=False)
    nombre = models.CharField(max_length=30)
    dni = models.PositiveBigIntegerField()
    
class Profesor (models.Model):
    profesor = models.OneToOneField(User, on_delete=models.CASCADE)
    legajo = models.IntegerField()

class Categoria (models.Model):
    nombre = models.CharField(max_length= 20,unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()

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
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)


class CursoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

class CategoriaManager(models.Manager):
    def cursos_por_categoria(self):
        
        return


class Curso (models.Model):
    GRATUITO = 'GR'
    PAGO = 'PA'
    CONDICION_CHOICES = [
        (GRATUITO, 'Gratuito'),
        (PAGO, 'Pago'),
    ]
    
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)
    duracion = models.IntegerField()
    cant_leccion = models.IntegerField()
    plan_estudios = models.CharField(max_length=100)
    condicion = models.CharField(max_length=2, choices=CONDICION_CHOICES, default=GRATUITO)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    objects = models.Manager()
    cursos_objects = CursoManager()
    

class Modulo (models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)

class Leccion (models.Model):
    tema = models.CharField(max_length=40)
    duracion = models.TimeField()
    modulo = models.ForeignKey(Modulo,on_delete=models.CASCADE)

class FavoritoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

class Favorito (models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
   
    objects = models.Manager()
    favoritos_objects = FavoritoManager()
    def __str__(self):
        return f"{self.alumno}"
    

class BusquedaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

class Busqueda (models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    
    objects = models.Manager()
    busqueda_objects = BusquedaManager()

class CursosImagenesManage(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

# se ahorra hacer el join entre curso imagen para usando la propiedad vista en la filmina 

class Imagen (models.Model):
    arch_imagen = models.FileField(upload_to='imagenes/')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Video (models.Model):
    arch_video = models.FileField(upload_to='videos/')
    video = models.ForeignKey(Leccion, on_delete=models.CASCADE)



