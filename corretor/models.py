from django.db import models
from usuarios.models import Aluno, Professor

class Exercicio(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(auto_now_add=True)
    xml_base = models.TextField()
    xml_base_grafo = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo

class Instituicao(models.Model):
    nome=models.CharField(max_length=100)
    instituicao_nova=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome=models.CharField(max_length=20)
    instituicao=models.ForeignKey(Instituicao,on_delete=models.CASCADE,related_name='turmas')
    professor=models.ForeignKey(Professor,on_delete=models.PROTECT,related_name='turmas')

    def __str__(self):
        return self.nome

class Desafio(models.Model):
    titulo=models.CharField(max_length=50)
    descricao=models.TextField()
    data_inicio=models.DateTimeField()
    data_final=models.DateTimeField()
    max_tentativas=models.PositiveIntegerField(null=True,blank=True)
    turma=models.ForeignKey(Turma,on_delete=models.PROTECT,related_name='desafios')
    criado_por=models.ForeignKey(Professor,on_delete=models.PROTECT,related_name='desafios')
    exercicios=models.ManyToManyField(Exercicio,related_name='desafios')

    def __str__(self):
        return self.descricao


class Submissao(models.Model):
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE,related_name='submissoes')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE,related_name='submissoes')
    desafio=models.ForeignKey(Desafio,on_delete=models.CASCADE,null=True,blank=True,related_name='submissoes')
    data_submissao = models.DateTimeField(auto_now_add=True)
    xml_submetido = models.TextField()
    resultado = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-data_submissao']

    def __str__(self):
        return f'{self.aluno} → {self.exercicio}' 





