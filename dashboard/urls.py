from django.urls import path
from dashboard import views
from dashboard import views_charts

urlpatterns = [
    path('aluno/', views.dashboard_aluno, name='dashboard_aluno'),
    path('professor/', views.dashboard_professor, name='dashboard_professor'),
    path('cadastro/',views.criar_turma,name='cadastro_turma'),
    path('api/charts/aluno-por-turma/',views_charts.aluno_por_turma,name='aluno_por_turma'),
    path('api/charts/numero-de-submissoes/',views_charts.aluno_por_turma,name='numero-submissoes')

]