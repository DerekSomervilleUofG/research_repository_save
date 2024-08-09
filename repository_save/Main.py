from repository_save.population_mapping.ControlPopulate import ControlPopulate
from utility.ReadWriteFile import ReadWriteFile
from repository_save.data_source.DatabaseCreate import DatabaseCreate
import sys

class Main():
    
    def __init__(self) -> None:
        self.control_populate = ControlPopulate()
        self.database_create = DatabaseCreate(self.control_populate.get_db_execute_sql())
        self.read_write_file = ReadWriteFile()
    
    def before_processing(self):
        pass
    
    def process_database(self, database):
        print(database)

    def after_processing(self):
        pass

    def database_setup(self):
        self.database_create.setup()
        
    def main(self, directory):
        self.before_processing()
        for database in self.read_write_file.get_list_from_directory(directory):
            if ".db" in database:
                self.control_populate.set_db_file_name(directory + database)
                self.database_setup()
                self.process_database(database)
        self.after_processing()

