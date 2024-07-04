from django import forms
from app_cursosit.models import *
from django.contrib.auth.forms import UserCreationForm


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name','email','password']

# class UserForm(forms.Form):
#     first_name = forms.CharField(required=True, max_length=40)
#     last_name = forms.CharField(required=True, max_length=40)
#     email = forms.EmailField(required=True)
    


# class UsuarioForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['','','']


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# class RegistroForm(UserCreationForm):
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = User
#         fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

#     def __init__(self, *args, **kwargs):
#         super(RegistroForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['password1'].widget.attrs['class'] = 'form-control'
#         self.fields['password2'].widget.attrs['class'] = 'form-control'





class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre','duracion','cant_leccion','descripcion',
                  'plan_estudios','condicion','categoria','precio',
                  ]