from repository_save.population_mapping.ControlPopulate import ControlPopulate
from repository_save.data_source.DatabaseCreate import DatabaseCreate
from repository_save.data_source.DBConnection import DBConnection
from repository_save.class_structure.Repository import Repository
from repository_save.class_structure.DeveloperCommit import DeveloperCommit
from repository_save.class_structure.File import File
from repository_save.class_structure.ClassStructure import ClassStructure
from repository_save.class_structure.Method import Method
from repository_save.class_structure.Developer import Developer
from repository_save.version_control.VersionControlGit import VersionControlGit
from class_structure.AmendmentType import *

class Main():

    def __init__(self) -> None:
        self.db_connection = DBConnection()
        self.control_populate = ControlPopulate()
        self.database_create = DatabaseCreate()
        self.db_connection.set_db_file_name("Test.db")
        self.database_create.setup()

    def test_run_class_structure(self):
        repository = Repository("https://stgit.dcs.gla.ac.uk/DerekSomerville/marking.git")
        developer = Developer("Derek Somerville", "derek.somerville@glasgow.ac.uk")
        developer_commit = DeveloperCommit("1234", "Derek Somerville", "27-Jun-2024", "Test", repository, developer)
        repository.add_commit(developer_commit)
        file = File("Test.py", added)
        developer_commit.add_file(file)
        class_structure = ClassStructure("ClassName", added, file)
        file.add_class(class_structure)
        method = Method("method_name", added, class_structure)
        class_structure.add_method(method)
        self.control_populate.save_all()
        
    def test_run_developer_batch(self):
        for counter in range(1000):
            developer = Developer(str(counter), "email@test.com")
        self.control_populate.save_all()
        populate_developer = self.control_populate.get_populate_developer()
        select_cursor = populate_developer.prepare_batch_select()
        developers = populate_developer.next_batch_select(select_cursor, 10)
        print("First batch", developers)
        print("Second batch", populate_developer.next_batch_select(select_cursor, 5))
        select_cursor.close()

    def version_control(self):
        version_control_git = VersionControlGit()
        repo = version_control_git.get_repo("output/dummy-repo","https://github.com/DerekSomervilleUofG/dummy-repo.git")
        print("Number of commits", len(version_control_git.get_commits_on_branch(repo, None, None)))
        
def main():
    main = Main()
    main.version_control()
    main.test_run_class_structure()
    main.test_run_developer_batch()

if __name__ == "__main__":
    main()
