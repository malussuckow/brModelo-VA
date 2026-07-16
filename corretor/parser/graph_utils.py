
def extract_by_type(graph,tipo):
    return[attrs['name'] for node_id,attrs in graph.nodes(data=True) if attrs['type'] == tipo]


def extract_cardinality_edge(graph):
    return [
        (graph.nodes[origem]['name'], graph.nodes[destino]['name'], attrs['cardinalidade'])
        for origem, destino, attrs in graph.edges(data=True)
        if attrs['type'] in ['PARTICIPATES', 'CONNECTS']
    ]