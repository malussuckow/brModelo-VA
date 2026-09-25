from django.urls import path
from desafio import views

urlpatterns = [
path('professor/', views.desafios,name='desafio_professor'),
path('aluno/',views.desafios_alunos,name='desafio_alunos'),
]