from repository_save.population_mapping.ControlPopulate import ControlPopulate
from utility.ReadWriteFile import ReadWriteFile
from repository_save.data_source.DatabaseCreate import DatabaseCreate
from utility.Communication import Communication
from utility.UtilityText import UtilityText

class Main():
    
    failure_report = "failed_database.csv"
    read_write_file = ReadWriteFile()
    control_populate = ControlPopulate()
    communication = Communication()
    exclusive_lock = True
    email_to = "derek.somerville@glasgow.ac.uk"
    database_already_complete = []

    def __init__(self) -> None:
        self.database_create = DatabaseCreate(self.control_populate.get_db_execute_sql())
    
    def set_exclusive_lock(self):
        self.control_populate.get_db_execute_sql().set_exclusive_lock(self.exclusive_lock)
    
    def before_processing(self):
        pass
    
    def process_database(self, control_populate):
        print(control_populate.get_db_execute_sql().get_database_name())

    def after_processing(self):
        if self.read_write_file.file_exists(self.failure_report):
            errors = self.read_write_file.get_file_as_string(self.failure_report)
            self.communication.send_email("derek.somerville@glasgow.ac.uk", "DATABASE FAILURE: ", errors)
            

    def database_setup(self):
        self.database_create.setup()

    def raise_exception(self, ex):
        raise ex 

    def handle_database_exception(self, ex, database):
        self.communication.send_email(self.email_to, "FAILURE REPSITORY_SAVE.MAIN: " + database, str(ex))
        self.read_write_file.append_to_file(self.failure_report, database + "," + UtilityText.formate_text(str(ex)))
        self.raise_exception(ex)

    def process_each_database(self, database):
        self.communication.send_email(self.email_to, "Start Process Database: " + database, "Processing database " + database)
        self.set_exclusive_lock()
        self.control_populate.set_db_file_name(database)
        self.database_setup()
        try:
            self.process_database(self.control_populate)
        except Exception as ex:
            self.handle_database_exception(ex, database)
        self.communication.send_email("derek.somerville@glasgow.ac.uk", "Completed Database: " + database, "Completed database " + database)
        

    def process_directory(self, directory):
        for database in self.read_write_file.get_list_from_directory(directory):
            if ".db" in database and database not in self.database_already_complete:
                self.process_each_database(directory + database)    
        
    def main(self, path):
        self.before_processing()
        if self.read_write_file.dir_exists(path):
            self.process_directory(path)
        elif ".db":
            self.process_each_database(path)
        self.after_processing()

