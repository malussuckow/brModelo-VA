from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class CadastroForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    tipo_usuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO, widget=forms.RadioSelect)

    class Meta:
        model = Usuario
        fields = ['username',
                'first_name', 
                'email', 
                'tipo_usuario',
                'password1', 
                'password2']
    
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
        