from django.shortcuts import redirect, render
from usuarios.forms import  CadastroForm, LoginForm
from usuarios.models import Aluno,Professor
from django.contrib.auth import authenticate, login as auth_login

def cadastro(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.tipo_usuario = form.cleaned_data['tipo_usuario']
        usuario.save()
        if usuario.tipo_usuario == 'aluno':
            Aluno.objects.create(usuario=usuario)
        else:
            Professor.objects.create(usuario=usuario)
        return redirect('login')
    return render(request, 'usuarios/cadastro.html', {'form': form})


def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            auth_login(request, usuario)
            if usuario.tipo_usuario == 'professor':
                return redirect('upload_professor')  # Redireciona para a página de upload do professor
            else:
                return redirect('upload_aluno') # Redireciona para a página de upload do aluno 
        else:
            form.add_error(None, 'Usuário ou senha inválidos')
    return render(request, 'usuarios/login.html', {'form': form})


