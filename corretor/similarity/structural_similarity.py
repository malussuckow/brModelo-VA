from xml.etree import ElementTree as ET 


def CalcularSimilaridade(a,b):
    if (a == 0 and b == 0):
        return 100.0
    else:
        menor = min(a, b)
        maior = max(a, b)
        similaridade=(menor / maior) * 100
        return round(similaridade, 2)
    

def Structural_Similarity(xml_base, xml_submetido):
        #contar entidades 
        count_entidades_base = len(xml_base.findall('Entidade'))
        count_entidades_submetido = len(xml_submetido.findall('Entidade'))
        sim_entidades=CalcularSimilaridade(count_entidades_base,count_entidades_submetido)
        
        #contar relacionamentos
        count_relacionamentos_base = len(xml_base.findall('Relacionamento'))
        count_relacionamentos_submetido = len(xml_submetido.findall('Relacionamento'))
        sim_relacionamentos=CalcularSimilaridade(count_relacionamentos_base,count_relacionamentos_submetido)

        #contar atributos
        count_atributos_base = len(xml_base.findall('Atributo'))
        count_atributos_submetido = len(xml_submetido.findall('Atributo'))
        sim_atributos=CalcularSimilaridade(count_atributos_base-count_atributos_submetido)

        resultado_final= round((sim_entidades+sim_relacionamentos+sim_atributos)/3,2)
            
        return resultado_final

def neighborhood_similarity():
    pass
