from django.contrib import admin
from perros.models import Perro, PerroAdmin, Persona, PersonaAdmin, PP


admin.site.register(Perro, PerroAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(PP)
