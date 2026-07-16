from rapidfuzz import process,fuzz

def match_words(text_professor,text_aluno):
    match_Word ={}

    for element_a in text_professor:

        resultado=process.extractOne(query=element_a,choices=text_aluno,scorer=fuzz.ratio,score_cutoff=60)

        if resultado is not None:
            melhor_match,score,indice=resultado

            score_normalizado=round(score/100,2)

            match_Word[element_a]={
                "match": melhor_match,
                'score': score_normalizado
            }

        else:
            match_Word[element_a]={
                "match": "Não há correspondencia",
                "score" : 0
            }

    return match_Word

