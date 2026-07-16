from corretor.domain.entity import Entity
from corretor.domain.attribute import Attribute
from corretor.domain.relationship import Relationship
from corretor.parser.graph_builder import build_graph
from corretor.normalization.logic_normalization import logicNormalization

def extract_schema(root):

    entities = []             
    relacionships = []
    attributes = []
    ligacoes = []

    for element in root.iter():
        if element.tag == 'Entidade':
            entity = Entity(element.attrib['ID'], element.find('Texto').text)
            entities.append(entity)

        elif element.tag == 'Relacionamento':
            relationship = Relationship(element.attrib['ID'], element.find('Texto').text)
            relacionships.append(relationship)

        elif element.tag == 'Atributo':
            attribute = Attribute(element.attrib['ID'],element.find('Texto').text,element.find('Identificador').attrib['Valor'] == 'true',element.find('Multivalorado').attrib['Valor'] == 'true',element.find('Opcional').attrib['Valor'] == 'true')
            attributes.append(attribute)

    for element in root.iter('Ligacao'):
        ligacao = element.find('Ligacoes') 
        if ligacao is not None:
            ponta_A = ligacao.attrib['PontaA']
            ponta_B = ligacao.attrib['PontaB']
            cardinalidade_card = element.find('Cardinalidade')
            if cardinalidade_card is not None:
                cardinalidade = cardinalidade_card.find('Card').attrib['Valor']
            else:
                cardinalidade = None
                
            ligacoes.append((ponta_A, ponta_B, cardinalidade))


    entities,relacionships,attributes=logicNormalization(entities,relacionships,attributes)

    graph = build_graph(entities, relacionships, attributes, ligacoes)

    return graph