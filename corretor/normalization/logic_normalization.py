from corretor.normalization.text_normalizer import textNormalizer
from corretor.normalization.singularizer import singlarizerText


def logicNormalization(entities,relationships,attributes):

    for entity in entities:
        entity.name=textNormalizer(entity.name)
        entity.name=singlarizerText(entity.name)

    for relationship in relationships:
        relationship.name=textNormalizer(relationship.name)
        relationship.name=singlarizerText(relationship.name)

    for attribute in attributes:
        attribute.name=textNormalizer(attribute.name)
        attribute.name=singlarizerText(attribute.name)

    return entities,relationships,attributes