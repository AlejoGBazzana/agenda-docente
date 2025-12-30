from django.db import models




class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puntaje = models.IntegerField(default=0)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Colegio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    dias_de_clases = models.CharField(max_length=100)
    horario_de_clases = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    turno = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    dias = models.CharField(max_length=100)
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True)
    edad = models.IntegerField()
    email = models.EmailField(blank=True)
    fecha_nacimiento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"