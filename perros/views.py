from django.shortcuts import render
from django.contrib import messages
from perros.forms import PersonaForm
from perros.models import Persona, PP, Perro


def listar_perros(request):
    articulo = Perro.objects.all()
    return render (request,'perros/listar_perros.html', {'articulo':articulo})


def perro_nuevo(request):
    if request.method == "POST":
        formulario = PersonaForm(request.POST)
        if formulario.is_valid():

            persona = Persona.objects.create(nombre=formulario.cleaned_data['nombre'],apellido=formulario.cleaned_data['apellido'], dpi = formulario.cleaned_data['dpi'])
            for perro_id in request.POST.getlist('perros'):
               pp = PP(perro_id=perro_id, persona_id = persona.id)
               pp.save()
            messages.add_message(request, messages.SUCCESS, 'Persona Guardada Exitosamente')
    else:
        formulario = PersonaForm()
    return render(request, 'perros/Persona_editar.html', {'formulario': formulario})
