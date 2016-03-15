from phenopacket.models.Meta import *
from phenopacket.models.Organism import *
from phenopacket.models.Environment import *
from phenopacket.models.Condition import *
import logging


logger = logging.getLogger(__name__)


class PhenoPacket(object):
    """
    Top level phenopacket container
    """

    def __init__(self, packet_id=None, title=None, entities=[], variants=[], persons=[],
                 organisms=[], phenotype_profile=[], diagnosis_profile=[],
                 environment_profile=[]):
        return

