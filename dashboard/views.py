from django.shortcuts import render,redirect
from dashboard.forms import CadastroTurmaForm,Desafios
from corretor.models import Turma
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def dashboard_aluno(request):
    return render(request,'aluno/dashboard_aluno.html')

@login_required
def dashboard_professor(request):
    turma = Turma.objects.filter(professor=request.user.professor)
    return render(request,'professor/dashboard_professor.html',{
        'turma': turma
    })

@login_required
def criar_turma(request):
    if request.method == 'POST':

        form = CadastroTurmaForm(request.POST)
        if form.is_valid():
            turma=form.save(commit=False)
            turma.professor=request.user.professor
            turma.save()
            return redirect('dashboard_professor')
    else:
        form=CadastroTurmaForm()

    return render(request,'professor/cadastrar_turma.html',{'form': form})

def desafios(request):
    if request.method == 'POST':

        form=Desafios(request.POST)
        if form.is_valid():
            desafio=form.save(commit=False)
            desafio.criado_por=request.user.professor
            desafio.save()
            messages.success(request, 'Desafio criado com sucesso!')
    else:
        form=Desafios()
    return render(request,'professor/cadastrar_desafios.html',{'form' : form})


def desafios_alunos(request):
    return render(request,'aluno/desafios_alunos.html')