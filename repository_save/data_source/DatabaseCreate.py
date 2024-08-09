from utility.ReadWriteFile import ReadWriteFile

class DatabaseCreate:
    
    read_write_file = ReadWriteFile()
    
    def __init__(self, db_execute_sql) -> None:
        self.db_execute_sql = db_execute_sql
        self.tables = ["repository", "developer", "developer_commit", "package", "file", "file_method", "class", "method", "commit_file", "commit_class", "commit_method"]
        self.delete_tables = []
        
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
        self.delete_all(self.delete_tables)


