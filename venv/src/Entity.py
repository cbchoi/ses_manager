
class Entity(object):
    def __init__(self, name):
        self.entity_name = name
    def __str__(self):
        return self.entity_name

### Test code ###
if __name__ == "__main__":
    print(Entity("abc"))
##################