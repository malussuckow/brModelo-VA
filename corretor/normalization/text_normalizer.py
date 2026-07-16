import re
from unidecode import unidecode 


def textNormalizer(texto):
    texto= texto.lower()
    texto = texto.lower()
    texto = re.sub(r'[_\-]', ' ', texto)   
    texto = unidecode(texto)
    texto = re.sub(r'[^a-z0-9\s]', '', texto)
    texto = re.sub(r'\s+', ' ', texto)
    return texto.strip()
