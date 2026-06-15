import networkx as nx 

def build_graph(entities,relacionships,attributes,ligacoes):
    G = nx.MultiDiGraph()

    for entity in entities:
        G.add_node(entity.id,name=entity.name,type='ENTITY')

    for relationship in relacionships:
        G.add_node(relationship.id,name=relationship.name,type='RELATIONSHIP')
    
    for attribute in attributes:
        G.add_node(attribute.id,name=attribute.name,type='ATTRIBUTE',identifier=attribute.identifier,multivalued=attribute.multivalued,optional=attribute.optional)
    

    for ponta_A, ponta_B, cardinalidade in ligacoes:
        if ponta_A not in G.nodes or ponta_B not in G.nodes:
            continue

        elif G.nodes[ponta_A]['type'] == 'ENTITY' and G.nodes[ponta_B]['type'] == 'RELATIONSHIP':
            G.add_edge(ponta_A, ponta_B,type='PARTICIPATES',cardinalidade=cardinalidade)

        elif G.nodes[ponta_A]['type'] == 'RELATIONSHIP' and G.nodes[ponta_B]['type'] == 'ENTITY':
            G.add_edge(ponta_A, ponta_B,type='CONNECTS',cardinalidade=cardinalidade)

        elif G.nodes[ponta_A]['type'] == 'ATTRIBUTE' and G.nodes[ponta_B]['type'] in ['ENTITY', 'RELATIONSHIP']:
            G.add_edge(ponta_A, ponta_B,type='HAS_ATTRIBUTE',cardinalidade=cardinalidade)

        elif G.nodes[ponta_A]['type'] in ['ENTITY', 'RELATIONSHIP'] and G.nodes[ponta_B]['type'] == 'ATTRIBUTE':
            G.add_edge(ponta_A, ponta_B,type='HAS_ATTRIBUTE',cardinalidade=cardinalidade)

        elif G.nodes[ponta_A]['type'] == 'ATTRIBUTE' and G.nodes[ponta_B]['type'] == 'ATTRIBUTE':
            G.add_edge(ponta_A, ponta_B,type='SUBATTRIBUTE',cardinalidade=cardinalidade)
            
    return G
