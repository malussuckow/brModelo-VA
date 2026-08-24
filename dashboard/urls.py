from django.urls import path
from dashboard import views

urlpatterns = [
    path('aluno/', views.dashboard_aluno, name='dashboard_aluno'),
    path('professor/', views.dashboard_professor, name='dashboard_professor'),
    path('cadastro/',views.criar_turma,name='cadastro_turma'),
    path('desafio/', views.desafios,name='desafio_professor'),
    path('desafios/',views.desafios_alunos,name='desafio_alunos')

]