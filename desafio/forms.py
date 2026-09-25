from django import forms
from corretor.models import Desafio

class Desafios(forms.ModelForm):
    class Meta:
        model=Desafio
        fields=['descricao','data_inicio',
                'data_final','max_tentativas',
                'turma','exercicios']

        widgets= {'data_inicio': forms.DateTimeInput(attrs={'type':'datetime-local'}),
                'data_final': forms.DateTimeInput(attrs={'type':'datetime-local'}),
                'exercicios':forms.CheckboxSelectMultiple() }


class Desafios_Alunos():
    pass