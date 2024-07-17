from class_structure.DeclaredStructure import DeclaredStructure
from utility.UtilityText import UtilityText
from class_structure.Variable import Variable


class Method(DeclaredStructure):

    def __init__(self, name, amendment, owned_by_class=None,
                 parameters=None, return_type="", primary_key=0):
        super().__init__(name, amendment, primary_key)
        if parameters is None:
            parameters = []
        self.owned_by_class = owned_by_class
        self.classes = owned_by_class
        self.parameters = parameters[:]
        self.return_type = return_type


    def set_owned_by_class(self, owned_by_class):
        self.owned_by_class = owned_by_class

    def get_variable_string(self):
        return self.get_declare().split("(")[1].split(")")[0]

    def get_return_type(self):
        return self.return_type

    def get_return_type_raw(self):
        return_type = ""
        start_of_declare = self.get_declare().split("(")[0]
        if " " in start_of_declare:
            declare_split = start_of_declare.split(" ")
            if len(declare_split) >= 2:
                return_type = declare_split[-2].strip()
        return return_type

    def get_variable(self):
        variables = []
        if len(self.lines) > 0 and "(" in self.lines[0]:
            input_variable_string = self.get_variable_string()
            for declare_variable in input_variable_string.split(","):
                declare_words = UtilityText.generate_words(declare_variable)
                if len(declare_words) > 1:
                    variables.append(Variable(declare_words[1], declare_words[0]))
        return variables

    def add_parameter(self, parameter_name, parameter_type):
        self.parameters.append((parameter_name, parameter_type))

    def get_parameter_names(self):
        return [i[0] for i in self.parameters]

    def get_parameter_types(self):
        return [i[1] for i in self.parameters]
    
    def __str__(self):
        return self.name
