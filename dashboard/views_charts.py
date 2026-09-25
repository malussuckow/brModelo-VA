from django.db.models import Count
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from corretor.models import Turma

@login_required
def aluno_por_turma(request):
    turmas=Turma.objects.filter(professor=request.user.professor).annotate(num_alunos=Count('alunos'))

    labels=[turma.nome for turma in turmas]
    data=[turma.num_alunos for turma in turmas]

    return JsonResponse({
        'labels': labels,
        'data': data
    })