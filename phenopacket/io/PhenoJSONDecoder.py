import json


class PhenoJSONDecoder(object):

    @staticmethod
    def decode_phenopacket(file):
        file_handle = open(file, 'r')
        contents = file_handle.readlines()
        json.loads(contents, object_hook=PhenoJSONDecoder.dict_to_phenopacket)

    @staticmethod
    def dict_to_phenopacket(dct):
        return

