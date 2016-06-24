import unittest
import os
import json
import python_jsonschema_objects as jsonobjects
import inspect
import pprint
pp = pprint.PrettyPrinter(indent=4)

from phenopacket.PhenoPacket import *
from phenopacket.models.Meta import *

class JsonToObjectTestCase(unittest.TestCase):
    """
    Test JSON to Python Object Mappers such as warlock and
    python_jsonschema_objects, see
    http://stackoverflow.com/questions/12465588/convert-a-json-schema-to-a-python-class
    """

    def setUp(self):
        schema_path = "../resources/schemas/phenopacket-level-1-schema.json"
        journal_path = "../resources/examples/journal-example-l2.json"

        schema_fh = open(os.path.join(os.path.dirname(__file__), schema_path), 'r')
        self.schema = json.load(schema_fh)

        journal_fh = open(os.path.join(os.path.dirname(__file__), journal_path), 'r')
        self.journal_example = json.load(journal_fh)

        builder = jsonobjects.ObjectBuilder(self.schema)
        self.namespace = builder.build_classes()

        schema_fh.close()
        journal_fh.close()

    def tearDown(self):
        pass

    def test_journal_generation(self):

        reference_pheno_packet = self.namespace\
            .UrnJsonschemaOrgMonarchinitiativePpkModelPhenopacket()\
            .from_json(json.dumps(self.journal_example))

        # We are going to build the PhenoPacket by constructing its terminal components
        # and then composing them until we get our final packet.

        # Add Entity(s)
        patient_1 = Entity(
                        id = "http://monarchinitiative.org/patient/1",
                        type = EntityType.patient)
                        # biological_sex = "female")

        patient_2 = Entity(
                        id = "http://monarchinitiative.org/patient/2",
                        type = EntityType.patient)
                        # biological_sex = "female")
        phenopacket_entities = [patient_1, patient_2]


        environment = Environment()
        severity = ConditionSeverity()
        onset = TemporalRegion()
        offset = TemporalRegion()

        # phenotype_1_1.onset = TemporalRegion()
        # phenotype_1_1.onset.types = [OntologyClass()]
        # phenotype_1_1.onset.types[0].id = "HP:0003593"
        # phenotype_1_1.onset.types[0].label = "Infantile onset"

        phenotype_1_1 = Phenotype(
                            environment=environment,
                            severity=severity,
                            onset=onset,
                            offset=offset)

        phenotype_association_1_1 = PhenotypeAssociation(
                                    entity = patient_1.id,
                                    evidence_list = [],     # Sequence[Evidence]=[],
                                    # created = "!!date 2016 2 9"
                                    phenotype = phenotype_1_1)

        phenotype_profile_1 = [phenotype_association_1_1]   # : Sequence[PhenotypeAssociation]=[]
        phenopacket = PhenoPacket(
                            packet_id = "packet1",
                            title = "Fatal infantile mitochondrial encephalomyopathy, hypertrophic cardiomyopathy and optic atrophy associated with a homozygous OPA1 mutation",
                            entities = phenopacket_entities,
                            # schema = "journal-example-level-1",
                            # '@context = "http://phenopacket.github.io/context/context.jsonld",
                            phenotype_profile = phenotype_profile_1)

        print(phenopacket)

        self.assertEqual(reference_pheno_packet.entities[0].id, reference_pheno_packet.entities[0].id)


if __name__ == '__main__':
    unittest.main()