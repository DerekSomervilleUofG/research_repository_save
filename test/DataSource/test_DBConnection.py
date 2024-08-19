from unittest import TestCase
from repository_save.data_source.DBConnection import DBConnection
from utility.ReadWriteFile import ReadWriteFile

class TestDBConnection(TestCase):
    
    db_connection = DBConnection()
    read_write_file = ReadWriteFile()
    database_one = "resource/database/test_one.db"
    database_two = "resource/database/test_two.db"
    database_second = "resource/database/test_second.db"
    database_three = "resource/database/test_three.db"
    database_four = "resource/database/test_four.db"
    database_five = "resource/database/test_five.db"
    
    def setUp(self):
        pass
        #self.read_write_file.delete_file(self.database_one)
        #self.read_write_file.delete_file(self.database_two)
        #self.read_write_file.delete_file(self.database_three)
        #self.read_write_file.delete_file(self.database_second)
        #self.read_write_file.delete_file(self.database_four)
        #self.read_write_file.delete_file(self.database_five)
    
    def test_set_db_file_name(self):
        self.db_connection.set_db_file_name(self.database_one)
        self.assertTrue(self.read_write_file.file_exists(self.database_one))
        
    def test_set_db_file_name_twice(self):
        self.db_connection.set_db_file_name(self.database_two)
        self.db_connection.set_db_file_name(self.database_second)
        self.assertTrue(self.read_write_file.file_exists(self.database_second))
        
    def test_set_db_file_name_twice_name(self):
        self.db_connection.set_db_file_name(self.database_three)
        self.db_connection.set_db_file_name(self.database_four)
        self.assertEqual(self.database_four, self.db_connection.sql_lite_url)
        
    def test_determine_database_name(self):
        self.assertEqual(self.database_four, self.db_connection.determine_database_name(self.database_four))
        
    def test_determine_database_name_stored(self):
        self.db_connection.determine_database_name(self.database_four)
        self.assertEqual(self.database_four, self.db_connection.sql_lite_url)
        
    def test_create_database(self):
        self.db_connection.create_database(self.database_five)
        self.assertTrue(self.read_write_file.file_exists(self.database_five))