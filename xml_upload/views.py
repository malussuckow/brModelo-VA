from django.shortcuts import render
from xml_upload.forms_professor import forms_xml_professor
from xml_upload.forms import Upload_xmlForm
from corretor.models import Exercicio, Submissao
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from corretor.services.logic_service import logic_service


@login_required(login_url='login')
def Upload_xml(request):
    exercicios = Exercicio.objects.all()
    form = Upload_xmlForm(request.POST or None, request.FILES or None)

    if  request.method == 'POST' and form.is_valid():
        
        exercicio= Exercicio.objects.get(id=request.POST.get('exercicio_id'))

        arquivo = form.cleaned_data['arquivo']
        conteudo_xml_submetido = arquivo.read().decode('utf-8')

        xml_base = exercicio.xml_base
        match_entidades,match_relacionamentos,match_atributos,media_geral = logic_service(xml_base,conteudo_xml_submetido)

        resultado_json = {
            'exercicio': exercicio.titulo,
            'id': request.user.username,
            'entidades': match_entidades,
            'relacionamentos': match_relacionamentos,
            'atributos':match_atributos,
            'media_geral':media_geral
        }

        Submissao.objects.create(
            exercicio=exercicio,
            xml_submetido=conteudo_xml_submetido,
            aluno=request.user.aluno,
            resultado=resultado_json
        )

        messages.success(request, 'Arquivos XML enviados com sucesso!')
        return render(request, 'upload_aluno.html', {'resultado': resultado_json, 'exercicios': exercicios, 'form': form})
        
    return render(request, 'upload_aluno.html', {'form': form, 'exercicios': exercicios})


@login_required(login_url='login')
def Upload_xml_professor(request):

    form = forms_xml_professor(request.POST or None, request.FILES or None)

    if  request.method == 'POST' and form.is_valid():

        arquivo = form.cleaned_data['xml_base']

        Exercicio.objects.create(
            titulo =form.cleaned_data['titulo'], 
            descricao =form.cleaned_data['descricao'],
            professor =request.user.professor,
            xml_base = arquivo.read().decode('utf-8')
        )
        messages.success(request, 'Atividade criada com sucesso!')

        return redirect('upload_professor')

    return render(request, 'upload_professor.html', {'form': form})


