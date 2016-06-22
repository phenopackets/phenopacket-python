from phenopacket.models.Organism import *
from phenopacket.models.Environment import *
from phenopacket.models.Condition import *
from phenopacket.models.Genome import *
from typing import Sequence


class PhenoPacket(object):
    """
    Top level phenopacket container
    """
    def __init__(self, packet_id: str=None, title: str=None,
                 entities: Sequence[Entity]=[], variants: Sequence[Variant]=[],
                 persons: Sequence[Person]=[], organisms: Sequence[Organism]=[],
                 phenotype_profile: Sequence[PhenotypeAssociation]=[],
                 diagnosis_profile: Sequence[DiseaseOccurrenceAssociation]=[],
                 environment_profile: Sequence[EnvironmentAssociation]=[]) -> None:

        self.id = packet_id
        self.title = title
        self.entities = entities
        self.variants = variants
        self.persons = persons
        self.organisms = organisms
        self.phenotype_profile = phenotype_profile
        self.diagnosis_profile = diagnosis_profile
        self.environment_profile = environment_profile

