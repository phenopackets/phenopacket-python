from phenopacket.models.Organism import *
from phenopacket.models.Environment import *
from phenopacket.models.Condition import *
from phenopacket.models.Genome import *
from typing import Sequence
import json
import inspect
from enum import Enum

class CustomEncoder(json.JSONEncoder):
    # def default(self, obj):
    #     if hasattr(obj, 'to_json'):
    #         return obj.to_json()
    #     if isinstance(obj, Enum):
    #         return obj.name
    #     return json.JSONEncoder.default(self, obj)

    def isempty(self, value):
        return (hasattr(value, '__len__') and len(value) == 0)

    def default(self, obj):
        # if hasattr(obj, "to_json"):
        #     return self.default(obj.to_json())
        if isinstance(obj, Enum):
            return obj.name
        elif hasattr(obj, "__dict__"):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj)
                if not key.startswith("__")
                and not inspect.isabstract(value)
                and not inspect.isbuiltin(value)
                and not inspect.isfunction(value)
                and not inspect.isgenerator(value)
                and not inspect.isgeneratorfunction(value)
                and not inspect.ismethod(value)
                and not inspect.ismethoddescriptor(value)
                and not inspect.isroutine(value)
                and not self.isempty(value)
                and not value is None
            )
            return self.default(d)
        return obj

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

    def __str__(self):
        return json.dumps(self, indent=2, sort_keys=True, cls=CustomEncoder)
