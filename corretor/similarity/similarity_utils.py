
def semantic_lexical_simlilarity(match_lexico,match_semantico):
    
    final_result={}
    for element_a,dados_lex in match_lexico.items():
        dados_sem = match_semantico[element_a]

        score_lex=dados_lex["score"]
        score_sem=dados_sem["score"]

        if score_lex >= score_sem:
            final_result[element_a] = {
                "match": dados_lex["match"],
                "score": score_lex
            }
        else:
            final_result[element_a] = {
                "match": dados_sem["match"],
                "score": score_sem
            }

    return final_result

