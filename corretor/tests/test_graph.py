import networkx as nx
import matplotlib.pyplot as plt
from corretor.parser import graph_builder
from corretor.parser import schema_extractor

def draw_graph(xml_submetido):
    entities, relacionships, attributes, ligacoes = schema_extractor.extract_schema(xml_submetido)
    graph = graph_builder.build_graph(entities, relacionships, attributes, ligacoes)

    pos = nx.kamada_kawai_layout(graph)
    
    node_colors = []
    for node in graph.nodes(data=True):
        if node[1]['type'] == 'ENTITY':
            node_colors.append('lightblue')
        elif node[1]['type'] == 'RELATIONSHIP':
            node_colors.append('lightgreen')
        elif node[1]['type'] == 'ATTRIBUTE':
            node_colors.append('lightcoral')

    labels = {node: data['name'] for node, data in graph.nodes(data=True)}

    nx.draw(graph, pos, labels=labels, node_color=node_colors, node_size=2500, font_size=8)
    #plt.show()
    return graph 