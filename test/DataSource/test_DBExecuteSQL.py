from unittest import TestCase
from repository_save.data_source.DBExecuteSQL import DBExecuteSQL
from utility.ReadWriteFile import ReadWriteFile

class TestDBExecuteSQL(TestCase):
    db_execute_sql = DBExecuteSQL()
    read_write_file = ReadWriteFile()
    
    def test_set_db_file_name(self):
        database = "resource/database/test.db"
        self.db_execute_sql.set_db_file_name(database)
        self.assertTrue(self.read_write_file.file_exists(database))
        
    def test_set_db_file_name_twice(self):
        database = "resource/database/test.db"
        self.db_execute_sql.set_db_file_name(database)
        database = "resource/database/test_second.db"
        self.db_execute_sql.set_db_file_name(database)
        self.assertTrue(self.read_write_file.file_exists(database))