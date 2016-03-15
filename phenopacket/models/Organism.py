from phenopacket.models.Meta import Entity
from phenopacket.models.Ontology import OntologyClass
from typing import Sequence


class Organism(Entity):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None, entity_id: str=None,
                 entity_label: str=None, entity_type: str=None,
                 taxon: OntologyClass=None, strain: OntologyClass=None,
                 sex: str=None, date_of_birth: str=None) -> None:
        super().__init__(types, negated_types, description,
                         entity_id, entity_label, entity_type)
        self.taxon = taxon
        self.strain = strain
        self.sex = sex
        self.date_of_birth = date_of_birth


class Person(Organism):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None, entity_id: str=None,
                 entity_label: str=None, entity_type: str=None,
                 taxon: OntologyClass=None, sex: str=None,
                 date_of_birth: str=None) -> None:
        super().__init__(types, negated_types, description,
                         entity_id, entity_label, entity_type,
                         taxon, sex=sex, date_of_birth=date_of_birth)