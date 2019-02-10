from Attribute import *

class Entity(object):
    def __init__(self, name):
        self.entity_name = name
        self.attribute_list = []

    def __str__(self):
        return self.entity_name

    def insert_attribute(self, attribute):
        self.attribute_list.append(attribute)
    def get_attribute_list(self):
        return self.attribute_list

### Test code ###
if __name__ == "__main__":
    entity = Entity("abc")
    entity.insert_attribute(ModelBehaviorAttribute())
    attribute : ModelBehaviorAttribute = entity.get_attribute_list()[0]
    attribute.insert_state("idle", 0)
    print(attribute.find_state("idle"))
    print(Entity("abc"))

##################