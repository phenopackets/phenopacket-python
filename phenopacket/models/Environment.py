from phenopacket.models.Ontology import ClassInstance
from phenopacket.models.Meta import Association
import logging

logger = logging.getLogger(__name__)


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

    def __init__(self, types=[], negated_types=[], description=None):
        super().__init__(types, negated_types, description)


class EnvironmentAssociation(Association):

    def __init__(self, entity=None, evidence_list=[], environment=None):
        super().__init__(entity, evidence_list, )
        if not isinstance(environment, Environment):
            logger.error("environment is not an instance of Environment")
