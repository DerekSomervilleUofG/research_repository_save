from repository_save.population_mapping.ControlPopulate import ControlPopulate
from class_structure.DeveloperCommit import DeveloperCommit as SuperClass
from repository_save.population_mapping.PopulatePackage import PopulatePackage
from repository_save.population_mapping.PopulateCommitFile import PopulateCommitFile
class DeveloperCommit(SuperClass):
    
    control_populate = ControlPopulate()
    store_repo_packages = True
    populate_package = PopulatePackage()
    populate_commit_file = PopulateCommitFile()

    def __init__(self, name, author, date, message, repository, developer):
        super().__init__(name, author, date, message, repository, developer)
        self.populate_structure = self.control_populate.get_populate_developer_commit()
        self.populate_structure.add_structure(self)
        
    def populate_packages(self, packages, prior_knowledge_id):
        for package in packages:
            self.populate_package.insert_package_and_file(package, self.name, self.repository.repository_id, prior_knowledge_id)

    def populate_commit_and_prior_knowledge(self):
        self.populate_packages(self.packages, 0)

    def populate_packages(self, commit_id, packages):
        populate_package = PopulatePackage()

    def populate_commit(self):
        self.populate_packages(self.name, self.packages)


        