from repository_save.population_mapping.ControlPopulate import ControlPopulate
from class_structure.Method import Method as SuperClass
class Method(SuperClass):
    
    control_populate = ControlPopulate()

    def __init__(self, name, amendment, owned_by_class=None, parameters=None, return_type="", primary_key=0):
        super().__init__(name, amendment, owned_by_class, parameters, return_type, primary_key)
        self.populate_structure = self.control_populate.get_populate_method()
        self.populate_commit = self.control_populate.get_populate_commit_method()
        self.populate_structure.add_structure(self)
        if owned_by_class.owned_by_file.developer_commit is not None:
            self.populate_commit.add_structure(self)