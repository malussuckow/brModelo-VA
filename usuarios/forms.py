from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario
from corretor.models import Instituicao, Turma


class CadastroForm(UserCreationForm):

    tipo_usuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO, widget=forms.RadioSelect)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    instituicao = forms.ModelChoiceField(queryset=Instituicao.objects.all(),label="Instituição de ensino",empty_label="Selecione sua instituição",required=False)
    turma = forms.ModelChoiceField(queryset=Turma.objects.all(),label="Turma",empty_label="Selecione sua turma",required=False)

    class Meta:
        model = Usuario
        fields = ['nome_completo',
                'username',
                'email', 
                'cpf',
                'tipo_usuario',
                'password1', 
                'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["nome_completo"].widget.attrs["placeholder"] = "ex: João Silva"
        self.fields["email"].widget.attrs["placeholder"] = "joaosilva@email.com"
        self.fields["password1"].widget.attrs["placeholder"] = "Senha"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirme sua senha"

        self.fields["password1"].label = "Senha"
        self.fields["password2"].label = "Confirmação de senha"

    def clean(self):
        cleaned_data = super().clean()
        tipo_usuario = cleaned_data.get('tipo_usuario')
        instituicao = cleaned_data.get('instituicao')
        turma = cleaned_data.get('turma')

        if tipo_usuario == 'professor' and not instituicao:
            self.add_error('instituicao', 'Selecione sua instituição de ensino.')

        if tipo_usuario == 'aluno' and not turma:
            self.add_error('turma', 'Selecione sua turma.')

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
        