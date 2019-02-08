from enum import Enum

### TODO-01 Define Error Type or Exception cbchoi

class AtributeType(Enum):
    BEHAVIOR = 0
    STRUCTURAL = 1
    UNKOWN_TYPE = -1

    def resolve_type(self, name):
        if "BEHAVIOR" == name.upper():
            return AtributeType.BEHAVIOR
        elif "STRUCTURAL" == name.upper():
            return AtributeType.STRUCTURAL
        else:
            print(name)
            return AttributeType.UNKOWN_TYPE