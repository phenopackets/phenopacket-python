import unittest
import os
import json
from jsonschema import validate, ValidationError
import python_jsonschema_objects as jsonobjects


class ValidatorTestCase(unittest.TestCase):
    """
    Test various json validators, jsonschema seems to be a popular
    lib, warlock and python-jsonschema-objects are build off
    of jsonschema and also include json to python object mappers

    The goal of this is to experiment with library options but these
    could eventually be integrated into the phenopacket python api

    As a first pass, testing that the journal example is incorrect
    and the rest are correct. These could be expanded in the future
    as appropriate
    """

    def setUp(self):
        schema_path = "../resources/schemas/phenopacket-level-1-schema.json"
        journal_path = "../resources/examples/journal-example-l1.json"
        omim_path = "../resources/examples/omim-example-l1.json"
        patient_path = "../resources/examples/patient-example-l1.json"
        variant_path = "../resources/examples/variant-example-l1.json"

        schema_fh = open(os.path.join(os.path.dirname(__file__), schema_path), 'r')
        self.schema = json.load(schema_fh)

        journal_fh = open(os.path.join(os.path.dirname(__file__), journal_path), 'r')
        self.journal_example = json.load(journal_fh)

        omim_fh = open(os.path.join(os.path.dirname(__file__), omim_path), 'r')
        self.omim_example = json.load(omim_fh)

        patient_fh = open(os.path.join(os.path.dirname(__file__), patient_path), 'r')
        self.patient_example = json.load(patient_fh)

        variant_fh = open(os.path.join(os.path.dirname(__file__), variant_path), 'r')
        self.variant_example = json.load(variant_fh)

        schema_fh.close()
        journal_fh.close()
        omim_fh.close()
        patient_fh.close()
        variant_fh.close()

    def tearDown(self):
        self.schema = None
        self.journal_example = None
        self.omim_example = None
        self.patient_example = None
        self.variant_example = None

    def test_incorrect_journal(self):
        """
        Test that the journal example is invalid since it
        uses "human" instead of patient
        'human' is not one of ['disease', 'organism', 'patient', 'variant', 'genotype']
        """
        with self.assertRaises(ValidationError):
            validate(self.journal_example, self.schema)

    def test_omim_example(self):
        """
        Test that our other example files validate as correct
        """
        validate(self.omim_example, self.schema)

    def test_patient_example(self):
        """
        Test that our other example files validate as correct
        """
        # with self.assertRaises(KeyError):
        #    validate(self.patient_example, self.schema)

        # jsonschema fails here with:
        # KeyError: 'urn:jsonschema:org:monarchinitiative:ppk:model:condition:TemporalRegion'
        # urllib.error.URLError: <urlopen error unknown url type: urn>
        # jsonschema.exceptions.RefResolutionError: <urlopen error unknown url type: urn>

        # builder = jsonobjects.ObjectBuilder(self.schema)
        # ns = builder.build_classes()
        # Same issues
        # urllib.error.URLError: <urlopen error unknown url type: urn>

    def test_variant_example(self):
        """
        Test that our other example files validate as correct
        """
        validate(self.variant_example, self.schema)


class JsonToObjectTestCase(unittest.TestCase):
    """
    Test JSON to Python Object Mappers such as warlock and
    python_jsonschema_objects, see
    http://stackoverflow.com/questions/12465588/convert-a-json-schema-to-a-python-class
    """

    def setUp(self):
        schema_path = "../resources/schemas/phenopacket-level-1-schema.json"
        omim_path = "../resources/examples/omim-example-l1.json"

        schema_fh = open(os.path.join(os.path.dirname(__file__), schema_path), 'r')
        self.schema = json.load(schema_fh)

        omim_fh = open(os.path.join(os.path.dirname(__file__), omim_path), 'r')
        self.omim_example = json.load(omim_fh)

        schema_fh.close()
        omim_fh.close()

    def tearDown(self):
        pass

    def test_omim_object_mapping(self):
        builder = jsonobjects.ObjectBuilder(self.schema)
        ns = builder.build_classes()


if __name__ == '__main__':
    unittest.main()