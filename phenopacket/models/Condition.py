from phenopacket.models.Ontology import ClassInstance
from phenopacket.models.Environment import Environment
from phenopacket.models.Meta import Association
from phenopacket.models.Ontology import OntologyClass
from typing import Sequence
import logging

logger = logging.getLogger(__name__)


class Assay(ClassInstance):
    """
    An instance of a type of assay that was performed to determine
    the presence or extent of a phenotype
    """

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None) -> None:
        super().__init__(types, negated_types, description)


class Condition(ClassInstance):
    """
    An abstract class that encompasses both DiseaseOccurrences and Phenotypes
    """

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None,
                 has_location=None, onset=None, offset=None, severity=None,
                 environment=None):
        super().__init__(types, negated_types, description)

        if not isinstance(environment, Environment):
            logger.error("environment is not an instance of Environment")

        if not isinstance(severity, ConditionSeverity):
            logger.error("severity is not an instance of ConditionSeverity")

        if not isinstance(onset, TemporalRegion):
            logger.error("onset is not an instance of TemporalRegion")

        if not isinstance(offset, TemporalRegion):
            logger.error("offset is not an instance of TemporalRegion")


class ConditionSeverity(ClassInstance):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None):
        super().__init__(types, negated_types, description)


class DiseaseStage(Condition):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None,
                 has_location=None, onset=None, offset=None, severity=None,
                 environment=None):
        super().__init__(types, negated_types, description, has_location,
                         onset, offset, severity, environment)



class DiseaseOccurrence(Condition):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None,
                 has_location=None, onset=None, offset=None, severity=None,
                 environment=None, stage=None):
        super().__init__(types, negated_types, description, has_location,
                         onset, offset, severity, environment)

        if not isinstance(stage, DiseaseStage):
            logger.error("stage is not an instance of DiseaseStage")


class DiseaseOccurrenceAssociation(Association):

    def __init__(self, entity=None, evidence_list=[], disease=None):
        super().__init__(entity, evidence_list)
        if not isinstance(disease, DiseaseOccurrence):
            logger.error("disease is not an instance of DiseaseOccurrence")


class Measurement(ClassInstance):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None,
                 unit=None, magnitude=None):
        super().__init__(types, negated_types, description)

        if not isinstance(unit, OntologyClass):
            logger.error("unit is not an instance of OntologyClass")


class OrganismalSite(ClassInstance):
    """
    An instance of a particular site on or in an organism. This may be
    a whole organ, a cell type or even a subcellular location.

    The type fields for this class are typically drawn from ontologies such
    as Uberon and CL.
    """

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None):
        super().__init__(types, negated_types, description)


class Phenotype(Condition):
    """
    An individual occurrence of a phenotype (a type of condition)
    """

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None,
                 has_location=None, onset=None, offset=None, severity=None,
                 environment=None, measurements=[]):

        super().__init__(types, negated_types, description, has_location,
                         onset, offset, severity, environment)

        if not all(isinstance(measurement, Measurement)
                   for measurement in measurements):
            logger.error("all values in measurements are instances Measurement")


class PhenotypeAssociation(Association):

    def __init__(self, entity=None, evidence_list=[], phenotype=None):
        super().__init__(entity, evidence_list)
        if not isinstance(phenotype, Phenotype):
            logger.error("phenotype is not an instance of Phenotype")


class TemporalRegion(ClassInstance):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None,
                 startTime=None, endTime=None):
        super().__init__(types, negated_types, description)
