from django.db.models import Count
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from corretor.models import Submissao

@login_required
def numero_submissoes(request):
    numero=Submissao.objects.filter(aluno=request.user.aluno).count

    return JsonResponse({
        'numero de submissões': numero
    })