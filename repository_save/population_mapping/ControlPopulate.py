from repository_save.population_mapping.PopulateRepository import PopulateRepository
from repository_save.population_mapping.PopulatePackage import PopulatePackage
from repository_save.population_mapping.PopulateFile import PopulateFile
from repository_save.population_mapping.PopulateClass import PopulateClass
from repository_save.population_mapping.PopulateMethod import PopulateMethod
from repository_save.population_mapping.PopulateDeveloper import PopulateDeveloper
from repository_save.population_mapping.PopulateDeveloperCommit import PopulateDeveloperCommit
from repository_save.population_mapping.PopulateCommitFile import PopulateCommitFile
from repository_save.population_mapping.PopulateCommitClass import PopulateCommitClass
from repository_save.population_mapping.PopulateCommitMethod import PopulateCommitMethod
from repository_save.data_source.DBExecuteSQL import DBExecuteSQL

class ControlPopulate:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if ControlPopulate.__instance is None:
            ControlPopulate.__instance = super(ControlPopulate, cls).__new__(cls, *args, **kwargs)
        return ControlPopulate.__instance

    def __init__(self) -> None:
        self.setup()

    def setup(self):
        self.db_execute_sql = DBExecuteSQL()
        self.populate_repository = PopulateRepository(self.db_execute_sql)
        self.populate_package = PopulatePackage(self.db_execute_sql)
        self.populate_file = PopulateFile(self.db_execute_sql)
        self.populate_class = PopulateClass(self.db_execute_sql)
        self.populate_method = PopulateMethod(self.db_execute_sql)
        self.populate_developer = PopulateDeveloper(self.db_execute_sql)
        self.populate_developer_commit = PopulateDeveloperCommit(self.db_execute_sql)
        self.populate_commit_file = PopulateCommitFile(self.db_execute_sql)
        self.populate_commit_class = PopulateCommitClass(self.db_execute_sql)
        self.populate_commit_method = PopulateCommitMethod(self.db_execute_sql)


    def save_all(self):
        self.populate_repository.save_rows()
        self.populate_developer.save_rows()
        self.save_package()
        self.save_commit()
        
    def save_package(self):
        self.populate_package.save_rows()
        self.populate_file.save_rows()
        self.populate_class.save_rows()
        self.populate_method.save_rows()
    
    def save_commit(self):
        self.populate_developer_commit.save_rows()
        self.populate_commit_file.save_rows()
        self.populate_commit_class.save_rows()
        self.populate_commit_method.save_rows()
    
    def set_db_file_name(self, db_file_name):
        self.db_execute_sql.set_db_file_name(db_file_name)
    
    def get_db_execute_sql(self):
        return self.db_execute_sql
    
    def get_populate_repository(self):
        return self.populate_repository
    
    def get_populate_package(self):
        return self.populate_package

    def get_populate_file(self):
        return self.populate_file
    
    def get_populate_class(self):
        return self.populate_class

    def get_populate_method(self):
        return self.populate_method

    def get_populate_developer(self):
        return self.populate_developer

    def get_populate_developer_commit(self):
        return self.populate_developer_commit

    def get_populate_commit_file(self):
        return self.populate_commit_file

    def get_populate_commit_class(self):
        return self.populate_commit_class

    def get_populate_commit_method(self):
        return self.populate_commit_method





