from repository_save.population_mapping.ControlPopulate import ControlPopulate
from class_structure.Developer import Developer as SuperClass
class Developer(SuperClass):
    
    control_populate = ControlPopulate()

    def __init__(self, name, email, login, primary_key=0):
        super().__init__(name, email, login, primary_key)
        self.populate_structure = self.control_populate.get_populate_developer()
        self.populate_structure.add_structure(self)

        