from phenopacket.models.Ontology import ClassInstance, OntologyClass
from enum import Enum
from typing import Sequence, List
import json

class EntityType(Enum):
    disease = 0
    organism = 1
    patient = 2
    variant = 3
    genotype = 4
    paper = 5


class Entity(ClassInstance):
    """
    An entity encompasses persons or non-human organisms,
    variants, diseases, genes, cohorts, etc
    """

    # Could also make a class if we need to expose to other classes
    # EntityType = Enum('EntityType', 'disease organism patient variant genotype paper')

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None, id: str=None,
                 label: str=None, type: str=None) -> None:

        if id is not None:
            if not isinstance(type, EntityType):
                raise TypeError("type is not one of valid"
                                " entity types {0}"
                                .format(list(EntityType)))

        super().__init__(types, negated_types, description)
        self.id = id
        self.label = label
        self.type = type

    def to_json(self):
        return self.__dict__



class Evidence(ClassInstance):
    """
    An instance of a type of evidence that supports an association
    The evidence model follows the GO model
    """

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None,
                 supporting_entities: List[str]=[], source: List[str]=[]) -> None:

        super().__init__(types, negated_types, description)
        self.supporting_entities = supporting_entities
        self.source = source


class Association(object):
    """
    An association connects an entity (for example, disease,
    person or variant) with either another entity, or with
    some kind of descriptor (for example, phenotype).

    All pieces of evidences are attached to associations
    """

    def __init__(self, entity: Entity=None,
                 evidence_list: Sequence[Evidence]=[]) -> None:
        self.entity = entity
        self.evidence_list = evidence_list


class Publication(object):

    def __init__(self, pub_id: str=None, title: str=None) -> None:
        self.id = pub_id
        self.title = title
