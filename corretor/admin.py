from django.contrib import admin
from .models import Instituicao, Turma, Exercicio, Desafio, Submissao

admin.site.register(Instituicao)
admin.site.register(Turma)
admin.site.register(Exercicio)
admin.site.register(Desafio)
admin.site.register(Submissao)
