from phenopacket.models.Meta import Entity
from phenopacket.models.Ontology import OntologyClass
from typing import Sequence


class GenomicEntity(Entity):
    # Add instance vars from Entity?
    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None, entity_id: str=None,
                 entity_label: str=None, entity_type: str=None,
                 taxon: OntologyClass=None) -> None:

        if not isinstance(taxon, OntologyClass):
            raise TypeError("taxon is not of type OntologyClass")

        super().__init__(types, negated_types, description,
                         entity_id, entity_label, entity_type)
        self.taxon = taxon


class Variant(GenomicEntity):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None, entity_id: str=None,
                 entity_label: str=None, entity_type: str=None,
                 taxon: OntologyClass=None,
                 description_hgvs: str=None) -> None:

        super().__init__(types, negated_types, description,
                         entity_id, entity_label, entity_type, taxon)
        self.description_hgvs = description_hgvs