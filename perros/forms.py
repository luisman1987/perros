from django import forms
from .models import Persona, Perro
from django.contrib.auth.models import User
from django.forms import ModelForm




class PersonaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Persona
        fields = ('nombre','apellido' ,'dpi','perros')


def __init__ (self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)

        self.fields["perros"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["perros"].help_text = "Ingrese los perros de cada Persona"
        self.fields["perros"].queryset = Perro.objects.all()

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
