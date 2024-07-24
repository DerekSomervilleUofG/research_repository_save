from repository_save.data_source.DBExecuteSQL import DBExecuteSQL
from utility.ReadWriteFile import ReadWriteFile
import sys

db_execute_sql = DBExecuteSQL()
read_write_file = ReadWriteFile()

class Main():
    
    def before_processing(self):
        pass
    
    def process_database(self, database):
        print(database)

    def after_processing(self):
        pass

    def main(self, directory):
        self.before_processing()
        for database in read_write_file.get_list_from_directory(directory):
            if ".db" in database:
                db_execute_sql.set_db_file_name(directory + database)
                self.process_database(database)
        self.after_processing()

