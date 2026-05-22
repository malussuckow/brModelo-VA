from django.shortcuts import render
from xml_upload.forms_professor import Upload_xml_professor
from corretor.views import Comparar_xml
from .forms import Upload_xmlForm
from corretor.models import Exercicio, Submissao
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def upload_xml(request):
    exercicios = Exercicio.objects.all()
    form = Upload_xmlForm(request.POST or None, request.FILES or None)

    if  request.method == 'POST' and form.is_valid():
        exercicio= Exercicio.objects.get(id=request.POST.get('exercicio_id'))
        arquivo = form.cleaned_data['arquivo']

        xml_base=exercicio.xml_base
        xml_submetido=arquivo.read().decode('utf-8')

        correcao=Comparar_xml(xml_base, xml_submetido)

        if correcao is None:
            messages.error(request, 'Erro ao processar o XML, Tente novemente!!')
            return render(request, 'upload_aluno.html', {'resultado': correcao})

        resultado_json = {
            'exercicio': exercicio.titulo,
            'id': request.user.username,
            'resultado da comparação':correcao
        }

        Submissao.objects.create(
            exercicio=exercicio,
            xml_submetido=xml_submetido,
            aluno=request.user.aluno,
            resultado = resultado_json
        )

        messages.success(request, 'Arquivos XML enviados com sucesso!')
        return render(request, 'upload_aluno.html', {'resultado_final' : correcao,'resultado': resultado_json, 'exercicios': exercicios, 'form': form})
   
        
    return render(request, 'upload_aluno.html', {'form': form, 'exercicios': exercicios})


@login_required(login_url='login')
def upload_xml_professor(request):
    form = Upload_xml_professor(request.POST or None, request.FILES or None)
    if  request.method == 'POST' and form.is_valid():
        arquivo = form.cleaned_data['xml_base']
        Exercicio.objects.create(
            titulo=form.cleaned_data['titulo'], 
            descricao=form.cleaned_data['descricao'],
            professor=request.user.professor,
            xml_base=arquivo.read().decode('utf-8')
        )
        messages.success(request, 'Atividade criada com sucesso!')

        return redirect('upload_professor')

    return render(request, 'upload_professor.html', {'form': form})



      

