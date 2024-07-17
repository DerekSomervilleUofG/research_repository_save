from class_structure.StructureWithCode import StructureWithCode

class DeclaredStructure(StructureWithCode):

    def __init__(self,name, amendment, primary_key=0):
        super().__init__(name, amendment, primary_key)
        self.declare = None

    def populate_declare(self):
        if len(self.lines) > 0:
            declare = self.lines[0]
        else:
            declare = ""
        found = False
        counter = 1
        while counter < len(self.lines) and not found:
            if ")" in declare:
                found = True
                delcare = declare.split(")")[0]
            else:
                declare += self.lines[counter]
            counter += 1
        return declare + ")"

    def get_declare(self):
        if self.declare is None:
            self.declare = self.populate_declare()
        return self.declare
