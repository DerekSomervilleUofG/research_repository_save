from repository_save.population_mapping.ControlPopulate import ControlPopulate
from class_structure.Package import Package as SuperClass
class Package(SuperClass):
    
    control_populate = ControlPopulate()

    def __init__(self, name, amendment, owned_by_file=None, primary_key=0):
        super().__init__(name, amendment, owned_by_file, primary_key)
        self.populate_structure = self.control_populate.get_populate_package()
        self.populate_structure.add_structure(self)
