import sys
from Entity import *
from Attribute import *
from Definition import *
import json
from collections import OrderedDict

class EntityManager(object):
    def __init__(self):
        self.entity_path = ""
        self.root_entity = None

    def set_entity_db_path(self, path):
        self.entity_path = path

    def retrive_entity_db_path(self):
        return self.entity_path

    def create_empty_entity_structure(self, type):
        enum = AttributeType.resolve_type_from_str(type)
        if enum == AttributeType.BEHAVIOR:
            return BehavioralEntity("")
        elif enum == AttributeType.STRUCTURAL:
            return StructuralEntity("")
        else:
            return Entity("")

    def create_system(self, entity:Entity):
        self.root_entity = entity

    def export_system_entity_structure(self, path="."):
        entity_data = OrderedDict()
        entity_data["name"] = self.root_entity.get_name()
        entity_data["attributes"] = self.root_entity.attribute_to_list()
        print(json.dumps(entity_data, ensure_ascii=False, indent="\t"))

    def export_system_entity_structure_recursively(self, path="."):
        entity_data = OrderedDict()
        entity_data["name"] = self.root_entity.get_name()
        entity_data["attributes"] = self.root_entity.attribute_to_list()
        print(json.dumps(entity_data, ensure_ascii=False, indent="\t"))

    def import_system_entity_structure(self, path="."):
        pass