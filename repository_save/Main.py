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
        
    def main(self, directory):
        self.before_processing()
        for database in self.read_write_file.get_list_from_directory(directory):
            if ".db" in database:
                self.communication.send_email("derek.somerville@glasgow.ac.uk", "Process Database: " + database, "Processing database " + database)
                self.control_populate.set_db_file_name(directory + database)
                self.database_setup()
                try:
                    self.process_database(self.control_populate)
                except Exception as ex:
                    self.communication.send_email("derek.somerville@glasgow.ac.uk", "FAILURE REPSITORY_SAVE.MAIN", str(ex))
                    raise ex
        self.after_processing()

