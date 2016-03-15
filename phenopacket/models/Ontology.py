from typing import Sequence


class ClassInstance(object):
    """
    An abstract class for anything that can be described
    as a boolean combination of ontology classes
    """

    def __init__(self, types: Sequence[OntologyClass]=[],
                 negated_types: Sequence[OntologyClass]=[],
                 description: str=None) -> None:
        return


class OntologyClass(object):

    def __init__(self, class_id=None, label=None) -> None:
        return


class PropertyValue(object):

    def __init__(self, property=None, filler=None) -> None:
        # Filler can be an object or string
        return


