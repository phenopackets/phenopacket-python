from phenopacket.models.Meta import Entity


class Organism(Entity):

    def __init__(self, taxon=None, sex=None, date_of_birth=None):
        return


class Person(Organism):

    def __init__(self, taxon=None, sex=None, date_of_birth=None):
        super().__init__(taxon=None, sex=None, date_of_birth=None)