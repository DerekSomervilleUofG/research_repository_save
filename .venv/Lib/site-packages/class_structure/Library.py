from class_structure.StructureWithCode import StructureWithCode


class Library(StructureWithCode):

    def __init__(self, name, amendment, alais, library_class_name, library_file_name, owner_by_file=None, owned_by_class=None, primary_key=0):
        super().__init__(name, amendment, primary_key)
        self.owner_by_file = owner_by_file
        self.owned_by_class = owned_by_class
        self.alais = alais
        self.library_class_name = library_class_name
        self.library_file_name = library_file_name
        self.variables = []

    def set_alais(self, alais):
        self.alais = alais

    def set_owned_by_file(self, owned_by_file):
        self.owner_by_file = owned_by_file

    def set_owned_by_class(self, owned_by_class):
        self.owned_by_class = owned_by_class

    def clear_variables(self):
        self.variables = []

    def add_variable(self, variable_name):
        if variable_name not in self.variables:
            self.variables.append(variable_name)