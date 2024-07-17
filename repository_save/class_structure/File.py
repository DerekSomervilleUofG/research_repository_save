from repository_save.population_mapping.ControlPopulate import ControlPopulate
from class_structure.File import File as SuperClass
class File(SuperClass):
    
    control_populate = ControlPopulate()

    def __init__(self, name, amendment, latest = "", package=None, primary_key=0):
        super().__init__(name, amendment, latest, package, primary_key)
        self.populate_structure = self.control_populate.get_populate_file()
        self.populate_commit = self.control_populate.get_populate_commit_file()
        self.populate_structure.add_structure(self)
        if self.developer_commit is not None:
            self.populate_commit.add_structure(self)