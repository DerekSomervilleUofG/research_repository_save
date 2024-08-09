from repository_save.data_source.DBExecuteSQL import DBExecuteSQL
from repository_save.population_mapping.PopulateStructure import PopulateStructure

class PopulateRepository(PopulateStructure):

    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.name = 1
        self.url = 2
        self.table_name = "repository"
        self.all_columns = "repository_id, name, url"
        self.primary_key = "repository_id"
       
    def generate_row(self, repository):
        return [repository.get_name(), repository.get_repo_path()]

    def generate_mapping(self, repository):
        insert_statement = "'" + repository.get_name() + "', "
        insert_statement += "'" + repository.get_repo_path()  + "'" 
        return insert_statement

if __name__ == "__main__":
    populate_repository = PopulateRepository()