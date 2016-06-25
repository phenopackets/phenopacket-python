from phenopacket.PhenoPacket import *
from phenopacket.models.Meta import *
import json

def gen_journal_packet():

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

gen_journal_packet()

