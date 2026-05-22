from urllib import request
from django.shortcuts import render
from .models import Exercicio, Submissao
from usuarios.models import Aluno, Professor
from xml.etree import ElementTree as ET 
from django.contrib.auth.decorators import login_required
from xml_upload.forms import Upload_xmlForm

def CalcularSimilaridade(a,b):
    if (a == 0 and b == 0):
        return 100.0
    else:
        menor = min(a, b)
        maior = max(a, b)
        similaridade=(menor / maior) * 100
        return round(similaridade, 2)
    

def Comparar_xml(xml_base, xml_submetido):
    try:
        tree_base = ET.fromstring(xml_base)

        tree_submetido = ET.fromstring(xml_submetido)

        #contar entidades 
        count_entidades_base = len(tree_base.findall('Entidade'))
        count_entidades_submetido = len(tree_submetido.findall('Entidade'))
        a=abs(((count_entidades_base - count_entidades_submetido)/count_entidades_base)*100)
        
        #contar relacionamentos
        count_relacionamentos_base = len(tree_base.findall('Relacionamento'))
        count_relacionamentos_submetido = len(tree_submetido.findall('Relacionamento'))
        b=abs(((count_relacionamentos_base - count_relacionamentos_submetido)/count_relacionamentos_base)*100)

        resultado_final = CalcularSimilaridade(a,b)
            

    except ET.ParseError:
        return None
        
    return resultado_final

        




