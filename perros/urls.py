from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls. static import static

urlpatterns = [
    #url(r'^$', views.lista_peliculas),
    url(r'^perro/nuevo/$', views.perro_nuevo, name='perro_nuevo'),
    url(r'^$', views.listar_perros, name='perro_listado'),
    ]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
