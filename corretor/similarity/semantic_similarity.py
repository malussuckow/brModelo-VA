from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_match(text_professor,text_aluno):
    match_semantic={}

    for element_a in text_professor:
        embeddings1=model.encode(element_a)
        melhor_score=-1
        melhor_match=None

        for element_b in text_aluno:
            embeddings2=model.encode(element_b)
            score=util.cos_sim(embeddings1,embeddings2)

            if score > melhor_score:
                melhor_score=score
                melhor_match=element_b

                if melhor_score > 0.35:
                    match_semantic[element_a]={
                        "match":melhor_match,
                        "score":round(melhor_score.item(),2)}
                
                else:
                    match_semantic[element_a]={
                        "match":"Não há nenhuma correspondencia",
                        "score":0
                    }
                                
                
    return match_semantic

