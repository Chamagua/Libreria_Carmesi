 # -*- coding: latin-1 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from decimal import Decimal
from django.db import models
from django.forms import ModelForm
from django.utils import timezone

# Create your models here.

class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio= models.CharField(max_length=50)
    ciudad= models.CharField(max_length=50)
    estado=models.CharField(max_length=60,default='San Salvador')
    pais=models.CharField(max_length=50)
    website= models.URLField(default='www.misitio.com')

    def __unicode__(self): # __unicode__ en Python 2
        return str(self.nombre)

    class Meta:
        ordering=['nombre']
        verbose_name_plural = "Editores"
#-----------------------------------------------------------------------------
class Autor(models.Model):
    nombre=models.CharField(max_length=30)
    apellidos= models.CharField(max_length=40)
    email=models.EmailField(default='correoautor@gmail.com')

    def __unicode__ (self):
        return '%s %s' % (self.nombre, self.apellidos) #'%s %s' %

    class Meta:
        verbose_name_plural = "Autores"
#------------------------------------------------------------------------

class Libro(models.Model):
    titulo= models.CharField(max_length=39)
    contenido= models.TextField(max_length=500, default='CONTENIDO VACIO')
    autores = models.ManyToManyField(Autor)
    categoria= models.CharField(max_length=20)
    editor= models.ForeignKey(Editor)
    #fecha_publicacion = models.DateField()
    portada= models.ImageField(upload_to='portadas')
    precio = models.DecimalField(max_digits=8, decimal_places=2,default = Decimal('0.00'))
    slug = models.SlugField(editable=False, blank=True, null=True)
    ISBN= models.CharField(max_length=20,default="00")


    def __unicode__(self): # __unicode__ en Python 2
        return str(self.titulo)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Libro, self).save(*args, **kwargs)
