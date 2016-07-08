from django.contrib import admin
from django.contrib.admin import AdminSite
from biblio.models import Editor, Autor, Libro
from django.utils.translation import ugettext_lazy
# Register your models here.
admin.site.register(Editor)
admin.site.register(Autor)
admin.site.register(Libro)

admin.site.site_header = 'Administracion Libreria Carmesi'
admin.site.site_title = 'Biblioteca-administracion'
admin.site.index_title = 'Gestion de Libreria Carmesi'
