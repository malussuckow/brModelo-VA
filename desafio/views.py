from django.shortcuts import render
from desafio.forms import Desafios
from corretor.models import Desafio
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404


def desafios(request):
    if request.method == 'POST':

        form=Desafios(request.POST)
        if form.is_valid():
            desafio=form.save(commit=False)
            desafio.criado_por=request.user.professor
            desafio.save()
            form.save_m2m() 
            messages.success(request, 'Desafio criado com sucesso!')
    else:
        form=Desafios()

    return render(request,'professores/cadastro_desafios.html',{'form' : form})


def desafios_alunos(request):
    return render(request,'alunos/desafio_alunos.html')
