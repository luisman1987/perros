from django.db import models
from django.contrib import admin

class Perro(models.Model):
    nombre  =   models.CharField(max_length=30)
    color  =   models.CharField(max_length=30)
    raza  =   models.CharField(max_length=30)
    imagen=models.FileField(null=True,blank=True)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre
class Persona(models.Model):
    nombre    = models.CharField(max_length=40)
    apellido    = models.CharField(max_length=40)
    dpi      = models.CharField(max_length=13)
    foto=models.FileField(null=True,blank=True)
    perros   = models.ManyToManyField(Perro, through='PP')
    def __str__(self):
        return self.nombre
class PP (models.Model):
    perro = models.ForeignKey(Perro, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
class PPInLine(admin.TabularInline):
    model = PP
    extra = 1

class PerroAdmin(admin.ModelAdmin):
    inlines = (PPInLine,)

class PersonaAdmin (admin.ModelAdmin):
    inlines = (PPInLine,)
