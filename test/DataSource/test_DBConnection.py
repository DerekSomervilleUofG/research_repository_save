from unittest import TestCase
from repository_save.data_source.DBConnection import DBConnection
from utility.ReadWriteFile import ReadWriteFile

class TestDBConnection(TestCase):
    
    db_connection = DBConnection()
    read_write_file = ReadWriteFile()
    
    def test_set_db_file_name(self):
        database = "resource/database/test.db"
        self.db_connection.set_db_file_name(database)
        self.assertTrue(self.read_write_file.file_exists(database))
        
    def test_set_db_file_name_twice(self):
        database = "resource/database/test.db"
        self.db_connection.set_db_file_name(database)
        database = "resource/database/test_second.db"
        self.db_connection.set_db_file_name(database)
        self.assertTrue(self.read_write_file.file_exists(database))
        
    def test_set_db_file_name_twice_name(self):
        database = "resource/database/test.db"
        self.db_connection.set_db_file_name(database)
        database = "resource/database/test_second.db"
        self.db_connection.set_db_file_name(database)
        self.assertEqual(database, self.db_connection.sql_lite_url)