from django import forms
from corretor.models import Turma,Desafio


class CadastroTurmaForm(forms.ModelForm):
    class Meta:
        model=Turma
        fields=['nome','instituicao']


class Desafios(forms.ModelForm):
    class Meta:
        model=Desafio
        fields=['descricao','data_inicio',
                'data_final','max_tentativas',
                'turma','exercicios']

        widgets= {'data_inicio': forms.DateTimeInput(attrs={'type':'datetime-local'}),
                'data_final': forms.DateTimeInput(attrs={'type':'datetime-local'}) }


class Desafios_Alunos():
    pass