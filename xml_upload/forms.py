from django import forms
from xml.etree import ElementTree as ET

class Upload_xmlForm(forms.Form):
    arquivo = forms.FileField()
    
    def clean_arquivo(self):
        arquivo_aluno= self.cleaned_data['arquivo']

        if not arquivo_aluno.name.endswith('.xml'):
            raise forms.ValidationError('Suporta apenas arquivos XML.')
        
        try:
            conteudo=arquivo_aluno.read().decode('utf-8')
            ET.fromstring(conteudo)
            arquivo_aluno.seek(0)
            
        except ET.ParseError as e:
            raise forms.ValidationError(f'O arquivo XML é inválido: {e}. Tente novamente.')
        
        return arquivo_aluno
    
    