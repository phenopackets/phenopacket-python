from phenopacket.models.Ontology import ClassInstance, OntologyClass
from phenopacket.models.Meta import Association, Entity, Evidence
from typing import Sequence


class Environment(ClassInstance):
    """
     An instance of any kind of environmental exposure. Here environment
     is defined broadly, and can include things as diverse as:

      - a history of smoking
      - living in a food desert
      - taking a particular type of drug at a certain regularity of a time interval
      - diet
      - microbiome
    """

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None,) -> None:
        super().__init__(types, negated_types, description)


class EnvironmentAssociation(Association):

    def __init__(self, entity: Entity=None,
                 evidence_list: Sequence[Evidence]=[],
                 environment: Environment=None) -> None:
        super().__init__(entity, evidence_list, )
        if not isinstance(environment, Environment):
            raise TypeError("environment is not of type Environment")

        self.environment = environment
