from phenopacket.models.Ontology import ClassInstance, OntologyClass
from enum import Enum
from typing import Sequence, List


class Entity(ClassInstance):
    """
    An entity encompasses persons or non-human organisms,
    variants, diseases, genes, cohorts, etc
    """

    # Could also make a class if we need to expose to other classes
    EntityType = Enum('EntityType', 'disease organism patient variant genotype')

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None, entity_id: str=None,
                 entity_label: str=None, entity_type: str=None) -> None:

        if entity_id is not None:
            if not isinstance(entity_type, self.EntityType):
                raise TypeError("type is not one of valid"
                                " entity types {0}"
                                .format(list(self.EntityType)))

        super().__init__(types, negated_types, description)
        self.id = entity_id
        self.label = entity_label
        self.entity_type = entity_type


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


class Publication(object):

    def __init__(self, pub_id: str=None, title: str=None) -> None:
        self.id = pub_id
        self.title = title


