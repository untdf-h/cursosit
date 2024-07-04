from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_cursosit.models import Profesor

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegistroProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        exclude = ['user']  # Excluye el campo 'user'

    def __init__(self, *args, **kwargs):
        # Pasar el usuario al formulario si se proporciona
        self.user = kwargs.pop('user', None)
        super(RegistroProfesorForm, self).__init__(*args, **kwargs)



class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


# class AlumnoForm(forms.ModelForm):
#     class Meta:
#         model = Alumno
#         fields = ['nombre', 'apellido', 'nacimiento']  # Campos específicos del alumno

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['nombre'].initial = self.instance.user.first_name
#         self.fields['apellido'].initial = self.instance.user.last_name
#         self.fields['nacimiento'].initial = self.instance.user.alumno.fecha_nacimiento