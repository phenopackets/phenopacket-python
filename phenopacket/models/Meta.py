from phenopacket.models.Ontology import ClassInstance
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class Entity(ClassInstance):
    """
    An entity encompasses persons or non-human organisms,
    variants, diseases, genes, cohorts, etc
    """

    # Could also make a class if we need to expose to other classes
    EntityType = Enum('EntityType', 'disease organism patient variant genotype')

    def __init__(self, types=[], negated_types=[], description=None,
                 entity_id=None, entity_label=None, entity_type=None):
        if not isinstance(entity_type, self.EntityType):
            logger.error("type is not one of valid"
                         " entity types {0}".format(list(self.EntityType)))
        super().__init__(types, negated_types, description)



class Association(object):
    """
    An association connects an entity (for example, disease,
    person or variant) with either another entity, or with
    some kind of descriptor (for example, phenotype).

    All pieces of evidences are attached to associations
    """

    def __init__(self, entity=None, evidence_list=[]):
        return


class Evidence(ClassInstance):
    """
    An instance of a type of evidence that supports an association
    The evidence model follows the GO model
    """

    def __init__(self, types=[], negated_types=[], description=None,
                 supporting_entities=[], source=[]):
        return


class Publication(object):

    def __init__(self, pub_id=None, title=None):
        return


