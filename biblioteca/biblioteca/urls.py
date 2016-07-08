"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from biblio import views
from biblio.contactos.views  import contactos
from biblio.views import IndexView, LibroDetailView, gracias, catego, lista_libros, ubicacion, add, remove, show,add_venta,Ventas



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^formsrc/$', views.formulario_buscar),
    url(r'^buscar/$', views.buscar),
    url(r'^contactos/$', contactos),
    url(r'^contactos/gracias/', gracias),
    url(r'^categoria/$',catego),
    url(r'^ubicacion/$',ubicacion),



    url(r'^libros/', lista_libros.as_view()),
    url(r'^$', IndexView.as_view()),
    url(r'^libro/(?P<slug>[-\w]+)/$', LibroDetailView.as_view()),


    url(r'^add/$', add),
    url(r'^remove/$', remove),
    url(r'^show/$', show.as_view()),


    url(r'^vendido/$',add_venta, name='padd'),

    url(r'^resumen/$', Ventas.as_view()),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
