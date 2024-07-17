from repository_save.data_source.DBExecuteSQL import DBExecuteSQL
from utility.ReadWriteFile import ReadWriteFile

class DatabaseCreate:


    db_execute_sql = DBExecuteSQL()
    read_write_file = ReadWriteFile()
    
    def __init__(self) -> None:
        self.tables = ["repository", "developer", "developer_commit", "package", "file", "file_method", "class", "method", "commit_file", "commit_class", "commit_method"]
        
    def drop(self, tables):
        for table in tables:
            self.db_execute_sql.execute_sql_command("DROP TABLE IF EXISTS " + table + ";")

    def delete_all(self, tables):
        for table in tables:
            self.db_execute_sql.execute_sql_command("delete from " + table + " where 1 = 1;")

    def create_tables(self, tables):
        directory = "resource/sql/"
        for table in tables:
            table_file_name =  table + ".sql"
            if self.read_write_file.file_exists(table_file_name, directory):
                create_table_sql = self.read_write_file.get_file_as_string(table_file_name, directory)
                self.db_execute_sql.execute_sql_command(create_table_sql)
                

    def setup(self):
        self.create_tables(self.tables)


