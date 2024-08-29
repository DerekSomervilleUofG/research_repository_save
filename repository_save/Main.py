from repository_save.population_mapping.ControlPopulate import ControlPopulate
from utility.ReadWriteFile import ReadWriteFile
from repository_save.data_source.DatabaseCreate import DatabaseCreate
from utility.Communication import Communication

class Main():
    
    read_write_file = ReadWriteFile()
    control_populate = ControlPopulate()
    communication = Communication()

    def __init__(self) -> None:
        self.database_create = DatabaseCreate(self.control_populate.get_db_execute_sql())
    
    def before_processing(self):
        pass
    
    def process_database(self, control_populate):
        print(control_populate.get_db_execute_sql().get_database_name())

    def after_processing(self):
        pass

    def database_setup(self):
        self.database_create.setup()

    def handle_database_exception(self, ex, database):
        self.communication.send_email("derek.somerville@glasgow.ac.uk", "FAILURE REPSITORY_SAVE.MAIN: " + database, str(ex))
        raise ex

    def process_each_database(self, database):
        self.communication.send_email("derek.somerville@glasgow.ac.uk", "Process Database: " + database, "Processing database " + database)
        self.control_populate.set_db_file_name(database)
        self.database_setup()
        try:
            self.process_database(self.control_populate)
        except Exception as ex:
            self.handle_database_exception(ex, database)
     

    def process_directory(self, directory):
        for database in self.read_write_file.get_list_from_directory(directory):
            if ".db" in database:
                self.process_each_database(directory + database)    
        
    def main(self, path):
        self.before_processing()
        if self.read_write_file.dir_exists(path):
            self.process_directory(path)
        elif ".db":
            self.process_database(path)
        self.after_processing()

