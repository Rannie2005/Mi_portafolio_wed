from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, max_length=300)
    imagen = models.ImageField(upload_to='cursos/')  # Imagen principal
    logo_institucion = models.ImageField(upload_to='cursos/', blank=True, null=True)
    insignia = models.ImageField(upload_to='cursos/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    

class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=300)
    imagen = models.ImageField(upload_to='cursos/')
    link_github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre