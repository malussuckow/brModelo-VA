from django import forms
import xml.etree.ElementTree as ET

class forms_xml_professor(forms.Form):

        titulo = forms.CharField(max_length=100)
        descricao = forms.CharField(widget=forms.Textarea)
        xml_base = forms.FileField()

        def clean_xml_base(self):
            arquivo = self.cleaned_data['xml_base']
            if not arquivo.name.endswith('.xml'):
                raise forms.ValidationError('Suporta apenas arquivos XML.')

            try:
                conteudo = arquivo.read().decode('utf-8')
                ET.fromstring(conteudo)
            except ET.ParseError as e :
                raise forms.ValidationError(f'Arquivo XML inválido:{e},Tente novamente.')
        
            arquivo.seek(0)
            return arquivo
    


