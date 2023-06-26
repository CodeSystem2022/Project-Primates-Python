from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=100)  # en vez de "nombre" en el original es "titulo"
    descripcion = models.TextField(blank=True)  # esto nos va a decir que el texto que vamos a ingresar es opccional

# con " python manage.py makemigrations " se migran las tablas creadas a la basse de datos
# con " python manage . py migrate " se crean las tablas en la base de datos