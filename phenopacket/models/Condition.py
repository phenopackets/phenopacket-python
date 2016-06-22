from phenopacket.models.Ontology import ClassInstance
from phenopacket.models.Environment import Environment
from phenopacket.models.Meta import Entity, Association, Evidence
from phenopacket.models.Ontology import OntologyClass
from typing import Sequence


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
                 has_location: str=None, onset: TemporalRegion=None,
                 offset: TemporalRegion=None, severity: ConditionSeverity=None,
                 environment: Environment=None) -> None:
        super().__init__(types, negated_types, description)

        if not isinstance(environment, Environment):
            raise TypeError("environment is not of type Environment")

        if not isinstance(severity, ConditionSeverity):
            raise TypeError("severity is not of type ConditionSeverity")

        if not isinstance(onset, TemporalRegion):
            raise TypeError("onset is not of type TemporalRegion")

        if not isinstance(offset, TemporalRegion):
            raise TypeError("offset is not of type TemporalRegion")

        self.has_location = has_location
        self.onset = onset
        self.offset = offset
        self.severity = severity
        self.environment = environment


class ConditionSeverity(ClassInstance):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None) -> None:
        super().__init__(types, negated_types, description)


class DiseaseStage(Condition):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None,
                 has_location: str=None, onset: TemporalRegion=None,
                 offset: TemporalRegion=None, severity: ConditionSeverity=None,
                 environment: Environment=None) -> None:
        super().__init__(types, negated_types, description, has_location,
                         onset, offset, severity, environment)


class DiseaseOccurrence(Condition):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None,
                 has_location: str=None, onset: TemporalRegion=None,
                 offset: TemporalRegion=None, severity: ConditionSeverity=None,
                 environment: Environment=None, stage: DiseaseStage=None) -> None:
        super().__init__(types, negated_types, description, has_location,
                         onset, offset, severity, environment)

        if not isinstance(stage, DiseaseStage):
            raise TypeError("stage is not of type DiseaseStage")

        self.stage = stage


class DiseaseOccurrenceAssociation(Association):

    def __init__(self, entity: Entity=None, evidence_list: Sequence[Evidence]=[],
                 disease: DiseaseOccurrence=None) -> None:
        super().__init__(entity, evidence_list)
        if not isinstance(disease, DiseaseOccurrence):
            raise TypeError("disease is not of type DiseaseOccurrence")

        self.disease = disease


class Measurement(ClassInstance):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None,
                 unit: OntologyClass=None, magnitude: str=None) -> None:
        super().__init__(types, negated_types, description)

        if not isinstance(unit, OntologyClass):
            raise TypeError("unit is not of type OntologyClass")

        self.unit = unit
        self.magnitude = magnitude


class OrganismalSite(ClassInstance):
    """
    An instance of a particular site on or in an organism. This may be
    a whole organ, a cell type or even a subcellular location.

    The type fields for this class are typically drawn from ontologies such
    as Uberon and CL.
    """

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None) -> None:
        super().__init__(types, negated_types, description)


class Phenotype(Condition):
    """
    An individual occurrence of a phenotype (a type of condition)
    """

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None, has_location: str=None,
                 onset: TemporalRegion=None, offset: TemporalRegion=None,
                 severity: ConditionSeverity=None,
                 environment: Environment=None,
                 measurements: Sequence[Measurement]=[]) -> None:

        super().__init__(types, negated_types, description, has_location,
                         onset, offset, severity, environment)

        if not all(isinstance(measurement, Measurement)
                   for measurement in measurements):
            raise TypeError("all values in measurements are not of type Measurement")

        self.measurements = measurements


class PhenotypeAssociation(Association):

    def __init__(self, entity: Entity=None,
                 evidence_list: Sequence[Evidence]=[],
                 phenotype: Phenotype=None) -> None:
        super().__init__(entity, evidence_list)
        if not isinstance(phenotype, Phenotype):
            raise TypeError("phenotype is not of type Phenotype")

        self.phenotype = phenotype


class TemporalRegion(ClassInstance):

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None,
                 start_time: str=None, end_time: str=None) -> None:
        super().__init__(types, negated_types, description)

        self.start_time = start_time
        self.end_time = end_time
