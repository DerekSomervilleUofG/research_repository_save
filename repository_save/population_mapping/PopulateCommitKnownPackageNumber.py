from repository_save.population_mapping.PopulateStructureIndividual import PopulateStructureIndividual
from repository_save.class_structure.CommitKnownPackageNumber import CommitKnownPackageNumber
from repository_save.population_mapping.ControlPopulate import ControlPopulate
from utility.UtilityText import UtilityText

class PopulateCommitKnownPackageNumber(PopulateStructureIndividual):

    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.table_name = "commit_known_package_number"
        self.all_columns = "commit_id, number_of_known_package_file, number_of_unknown_package_file, developer_id, repository_id"
        self.primary_key = ""
        self.foreign_key = "repository_id"

        self.primary_key_col = 0
        self.number_of_known_package_file = 1
        self.number_of_unknown_package_file = 2 
        self.foreign_key_col = 3

        self.sql_rows = []
        self.list_structures = []
        self.counter = 0

    def get_structure_rows(self):
        for structure in self.list_structures:
            self.sql_rows.append(self.generate_row(structure))


    def generate_row(self, known_package):
        return [known_package.get_commit_id(), known_package.get_number_of_known(), known_package.get_number_of_unknown(), known_package.get_developer_id(), known_package.get_repository_id()]
    
def main():
    control_populate = ControlPopulate()
    control_populate.db_execute_sql.set_db_file_name("resource/database/codebase.db")
    populate_commit_known_package = PopulateCommitKnownPackageNumber(control_populate.db_execute_sql)
    commit_known_package_number = CommitKnownPackageNumber("COMMIT123", 3, 2, 1)
    populate_commit_known_package.add_structure(commit_known_package_number)
    print(control_populate.db_execute_sql.get_database_name(), len(populate_commit_known_package.list_structures))
    populate_commit_known_package.save_rows()

