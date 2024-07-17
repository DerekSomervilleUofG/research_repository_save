from repository_save.population_mapping.ControlPopulate import ControlPopulate
from class_structure.Repository import Repository as SuperClass
class Repository(SuperClass):
    
    control_populate = ControlPopulate()

    def __init__(self, name, primary_key=0):
        super().__init__(name, primary_key)
        self.populate_structure = self.control_populate.get_populate_repository()
        self.populate_structure.add_structure(self)


if __name__ == "__main__":
    repository = Repository("https://stgit.dcs.gla.ac.uk/DerekSomerville/repository_structure_save")
    repository.populate_structure.save_rows()