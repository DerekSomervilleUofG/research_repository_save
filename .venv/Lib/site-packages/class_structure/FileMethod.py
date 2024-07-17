from class_structure.DeclaredStructure import DeclaredStructure

class FileMethod(DeclaredStructure):

    def __init__(self, name, amendment, owner_by_file=None, primary_key=0):
        super().__init__(name, amendment, primary_key)
        self.owner_by_file = owner_by_file
