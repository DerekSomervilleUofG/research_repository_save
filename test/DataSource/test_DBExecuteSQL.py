from unittest import TestCase
from repository_save.data_source.DBExecuteSQL import DBExecuteSQL
from utility.ReadWriteFile import ReadWriteFile

class TestDBExecuteSQL(TestCase):
    db_execute_sql = DBExecuteSQL()
    read_write_file = ReadWriteFile()
    
    database_one = "resource/database/db_execute_test_one.db"
    database_two = "resource/database/db_execute_test_two.db"
    database_second = "resource/database/db_execute_test_second.db"
    
    def setUp(self):
        pass
        #self.read_write_file.delete_file(self.database_one)
        #self.read_write_file.delete_file(self.database_two)
        #self.read_write_file.delete_file(self.database_second)
        
    def test_set_db_file_name(self):
        self.db_execute_sql.set_db_file_name(self.database_one)
        self.assertTrue(self.read_write_file.file_exists(self.database_one))
        
    def test_set_db_file_name_twice(self):
        self.db_execute_sql.set_db_file_name(self.database_two)
        self.db_execute_sql.set_db_file_name(self.database_second)
        self.assertTrue(self.read_write_file.file_exists(self.database_second))