from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Usuario(AbstractUser):
    TIPO_USUARIO = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )
    nome_completo=models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=30,choices=TIPO_USUARIO)
    cpf=models.CharField(max_length=11,unique=True,validators=[RegexValidator(r'^\d{11}$', 'CPF deve conter exatamente 11 dígitos numéricos.')])

    def __str__(self):
        return f'{self.username} ({self.get_tipo_usuario_display()})'


class Professor(models.Model):
    usuario = models.OneToOneField(Usuario,on_delete=models.CASCADE,related_name='professor',)
    aprovado = models.BooleanField(default=False)
    instituicao=models.ForeignKey('corretor.Instituicao',on_delete=models.CASCADE,related_name='professores')

    def __str__(self):
        return f'Prof. {self.usuario.get_full_name() or self.usuario.username}'


class Aluno(models.Model):
    usuario = models.OneToOneField(Usuario,on_delete=models.CASCADE,related_name='aluno',)
    turma=models.ForeignKey('corretor.Turma',on_delete=models.CASCADE,related_name='alunos')


    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username


