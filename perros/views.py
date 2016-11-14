from django.shortcuts import render
from django.contrib import messages
from perros.forms import PersonaForm
from perros.models import Persona, PP, Perro
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from perros.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect


@login_required()
def inicio(request):
    return render_to_response('perros/listar_perros.html', {'user': request.user}, context_instance=RequestContext(request))

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

def main(request):
    return render_to_response('perros/main.html', {}, context_instance=RequestContext(request))


def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass

            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name

            # Save new user attributes
            user.save()

            return HttpResponseRedirect(reverse('main'))  # Redirect after POST
    else:
        form = SignUpForm()

    data = {
        'form': form,
    }
    return render_to_response('perros/signup.html', data, context_instance=RequestContext(request))
