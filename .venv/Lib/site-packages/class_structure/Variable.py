from class_structure.Structure import Structure

class Variable(Structure):

    def __init__(self, name, type, primary_key=0):
        super().__init__(name, Structure.added, primary_key)
        self.type = type
