from corretor.parser.graph_utils import extract_by_type
from corretor.similarity.match import match_words
from corretor.similarity.semantic_similarity import semantic_match
import statistics
import itertools
from corretor.similarity.similarity_utils import semantic_lexical_simlilarity

def logic_similarity(graph_professor, graph_aluno):

    # --- ENTIDADES ---
    entidades_professor = extract_by_type(graph_professor, 'ENTITY')
    entidades_aluno = extract_by_type(graph_aluno, 'ENTITY')

    # --- RELACIONAMENTOS ---
    relacionamentos_professor = extract_by_type(graph_professor, 'RELATIONSHIP')
    relacionamentos_aluno = extract_by_type(graph_aluno, 'RELATIONSHIP')

    # --- ATRIBUTOS ---
    atributos_professor = extract_by_type(graph_professor, 'ATTRIBUTE')
    atributos_aluno = extract_by_type(graph_aluno, 'ATTRIBUTE')

    #----MATCHS-----
    match_entidades = match_words(entidades_professor, entidades_aluno)
    match_relacionamentos = match_words(relacionamentos_professor, relacionamentos_aluno)
    match_atributos = match_words(atributos_professor, atributos_aluno)

    #-----MATCHS SEMANTICOS 
    semantic_similarity_entidades=semantic_match(entidades_professor,entidades_aluno)
    semantic_similarity_relacionamentos=semantic_match(relacionamentos_professor,relacionamentos_aluno)
    semantic_similarity_atributos=semantic_match(atributos_professor,atributos_aluno)

    #-----------------COMBINAÇÃO
    final_entidades=semantic_lexical_simlilarity(match_entidades,semantic_similarity_entidades)
    final_relacionamentos=semantic_lexical_simlilarity(match_relacionamentos,semantic_similarity_relacionamentos)
    final_atributos=semantic_lexical_simlilarity(match_atributos,semantic_similarity_atributos)
    
    #-----MÉDIA GERAL
    chain_list_match= itertools.chain(final_entidades.values(),final_relacionamentos.values(),final_atributos.values())
    scores=[item['score'] for item in chain_list_match]
    total_score=statistics.mean(scores)

    return final_entidades,final_relacionamentos,final_atributos,(f"{total_score:.2f}")