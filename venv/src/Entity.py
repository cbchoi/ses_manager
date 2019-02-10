from Attribute import *
from collections import OrderedDict

class Entity(object):
    def __init__(self, name):
        self.entity_name = name
        self.attribute_list = []

    def __str__(self):
        return self.entity_name

    def set_name(self, name):
        self.entity_name = name
    def get_name(self):
        return self.entity_name

    def insert_attribute(self, attribute):
        self.attribute_list.append(attribute)
    def get_attribute_list(self):
        return self.attribute_list

class StructuralEntity(Entity):
    def __init__(self, name):
        super(StructuralEntity, self).__init__(name)
        self.attribute_list.append(ModelStructuralAttribute())

    def insert_entity(self, name):
        self.attribute_list[0].insert_entity(name)

    def insert_input_port(self, name):
        self.attribute_list[0].insert_input_port(name)
    def retrive_input_ports(self):
        return  self.attribute_list[0].retrive_input_ports()

    def insert_output_port(self, name):
        self.attribute_list[0].insert_output_port(name)
    def retrive_output_ports(self):
        return  self.attribute_list[0].retrive_output_ports()

    def insert_coupling(self, src, dst):
        self.attribute_list[0].insert_coupling(src, dst)

    def attribute_to_list(self):
        to_list = []
        attributes = self.get_attribute_list()
        for attribute in attributes:
            json_obj = OrderedDict()
            json_obj["type"] = AttributeType.resolve_type_from_enum(attribute.get_type())
            json_obj["entities"] = attribute.retrive_entities()
            json_obj["input_ports"] = attribute.retrive_input_ports()
            json_obj["output_ports"] = attribute.retrive_output_ports()
            json_obj["external_input"] = attribute.retrive_external_input_coupling()
            json_obj["external_output"] = attribute.retrive_external_output_coupling()
            json_obj["internal"] = attribute.retrive_internal_coupling  ()
            to_list.append(json_obj)
        return to_list
    pass

class BehaviorEntity(Entity):
    def __init__(self, name):
        super(BehaviorEntity, self).__init__(name)
        self.attribute_list.append(ModelBehavioralAttribute())

    pass

### Test code ###
if __name__ == "__main__":
    entity = Entity("abc")
    entity.insert_attribute(ModelBehaviorAttribute())
    attribute : ModelBehaviorAttribute = entity.get_attribute_list()[0]
    attribute.insert_state("idle", 0)
    print(attribute.find_state("idle"))
    print(Entity("abc"))

##################