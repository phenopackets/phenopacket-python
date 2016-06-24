from typing import Sequence
import json


class OntologyClass(object):

    def __init__(self, class_id: str=None, label: str=None) -> None:
        self.id = class_id
        self.label = label

    def to_json(self):
        return self.__dict__


class ClassInstance(object):
    """
    An abstract class for anything that can be described
    as a boolean combination of ontology classes
    """

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None) -> None:
        self.types = types
        self.negated_types = negated_types
        self.description = description

    def to_json(self):
        return self.__dict__


class PropertyValue(object):

    def __init__(self, prop: str=None, filler: str=None) -> None:
        # Filler can be an object or string
        self.property = prop
        self.filler = filler

    def to_json(self):
        return self.__dict__


