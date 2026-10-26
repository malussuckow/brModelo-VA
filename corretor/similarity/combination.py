
def semantic_lexical_simililarity(match_lexico,match_semantico):
    
    final_result={}

    for id_professor,dados_lexicos in match_lexico.items():
        dados_semanticos = match_semantico[id_professor]

        score_lexico=dados_lexicos["score"]
        score_semantico=dados_semanticos["score"]


        if score_lexico >= score_semantico:

            final_result[id_professor] = {
                "professor_correspondente":dados_lexicos["professor_correspondente"],
                "id_aluno_correspondente": dados_lexicos["id_aluno_correspondente"],
                "dado_aluno_correspondente":dados_lexicos["dado_aluno_correspondente"],
                "score": score_lexico
            }
        else:
            final_result[id_professor] = {
                "professor_correspondente":dados_semanticos["professor_correspondente"],
                "id_aluno_correspondente": dados_semanticos["id_aluno_correspondente"],
                "dado_aluno_correspondente":dados_semanticos["dado_aluno_correspondente"],
                "score": score_semantico
            }


    return final_result
