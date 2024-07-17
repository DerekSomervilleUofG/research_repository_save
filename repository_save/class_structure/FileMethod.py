from repository_save.population_mapping.ControlPopulate import ControlPopulate
from class_structure.FileMethod import FileMethod as SuperClass
class FileMethod(SuperClass):
    
    control_populate = ControlPopulate()

    def __init__(self, name, amendment, owned_by_file=None, primary_key=0):
        super().__init__(name, amendment, owned_by_file, primary_key)
        self.populate_structure = self.control_populate.get_populate_file_method()
        self.populate_commit = self.control_populate.get_populate_commit_file_method()
        self.populate_structure.add_structure(self)
        if owned_by_file.developer_commit is not None:
            self.populate_commit.add_structure(self)