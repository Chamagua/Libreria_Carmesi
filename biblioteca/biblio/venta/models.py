from __future__ import unicode_literals

from decimal import Decimal
from django.db import models
from django import forms
from django.forms import ModelForm
from django.utils import timezone


class Venta(models.Model):
    fecha = models.DateField(auto_now=True)
    total = models.DecimalField(max_digits=8, decimal_places=2,default = Decimal('0.00'), editable=False)
    nombre= models.CharField(max_length=39)
    tarjeta= models.CharField(max_length=39)
    fecha_expiracion= models.DateField(default="2015-05-24",help_text="Por favor use el siguiente formato: <em>YYYY-MM-DD</em>.")
    direccion = models.CharField(max_length=100)
    email = models.EmailField()

    def __unicode__(self):
        return self.id

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        exclude=()

    def clean_nombre(self):
      diccionario_limpio = self.cleaned_data

      nombre = diccionario_limpio.get('nombre')

      if nombre.isdigit():
         raise forms.ValidationError("ERROR:UN NOMBRE NO LLEVA NUMEROS")

      return nombre



    def clean_tarjeta(self):
        diccionario_limpio = self.cleaned_data
        tarjeta = diccionario_limpio.get('tarjeta')
        if not len(tarjeta)==16:
            raise forms.ValidationError("TARJETA INVALIDA DE FALTAN NUMEROS O LE SOBRAN NUMEROS")
            if not tarjeta.isdigit():
                raise forms.ValidationError("TARJETA INVALIDA UN NUMERO DE TARJETA NO LLEVA LETRAS")
        return tarjeta
