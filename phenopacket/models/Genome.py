from phenopacket.models.Meta import Entity


class GenomicEntity(Entity):

    def __init__(self, taxon=None):
        # TODO check if taxon is of type OntologyClass
        return


class Variant(GenomicEntity):

    def __init__(self, taxon=None, description_hgvs=None):
        super().__init__(taxon)
        return