from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include('perros.urls')),
    url(r'^$', 'perros.views.main', name='main'),
    url(r'^signup$', 'perros.views.signup', name='signup'),
    url(r'^login$', login, {'template_name': 'perros/login.html', }, name="login"),
    url(r'^home$', 'perros.views.listar_perros', name='home'),
    url(r'^logout$', logout, {'template_name': 'perros/main.html', }, name="logout"),
]
