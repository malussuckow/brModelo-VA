from corretor.parser.xml_parser import parse_xml
from corretor.parser.schema_extractor import extract_schema
from corretor.tests.test_graph import draw_graph
from corretor.similarity.logic_similarity import logic_similarity

def logic_service(xml_professor,xml_aluno):

    conteudo_xml_aluno= parse_xml(xml_aluno)
    extract_aluno=extract_schema(conteudo_xml_aluno)

    #draw_graph(conteudo_xml)
    
    conteudo_xml_professor = parse_xml(xml_professor)
    extract_professor=extract_schema(conteudo_xml_professor)

    return logic_similarity(extract_professor,extract_aluno)

