import spacy 

nlp = spacy.load("pt_core_news_sm")


def singlarizerText(texto):
    doc=nlp(texto)

    singluar_words=[token.lemma_ for token in doc]

    return " ".join(singluar_words)

