import xml.etree.ElementTree as ET


def parse_xml(conteudo_xml_submetido):
    try:
        tree_submetido = ET.fromstring(conteudo_xml_submetido)

        return tree_submetido

    except ET.ParseError:
        return None