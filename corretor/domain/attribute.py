class Attribute:
    def __init__(self,id, name, identifier= False, multivalued= False, optional= False):
        self.id = id
        self.name = name
        self.identifier = identifier
        self.multivalued = multivalued
        self.optional = optional