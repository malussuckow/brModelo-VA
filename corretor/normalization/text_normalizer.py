import re
from unidecode import unidecode 
from corretor.services.logic_parse import logic_service


def textNormalizer(texto):
    texto= texto.lower()
    texto = texto.lower()
    texto = re.sub(r'[_\-]', ' ', texto)   
    texto = unidecode(texto)
    texto = re.sub(r'[^a-z0-9\s]', '', texto)
    texto = re.sub(r'\s+', ' ', texto)
    return texto.strip()
