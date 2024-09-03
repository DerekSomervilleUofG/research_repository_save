import sqlite3
from repository_save.data_source.DBConnection import DBConnection

class DBExecuteSQL(object):

    db_connector = DBConnection()
    connection = None
    batch_size = 1000
    exclusive_lock = True
    
    def set_exclusive_lock(self, lock):
        self.exclusive_lock = lock
   
    def set_db_connector(self, db_connector):
        self.db_connector = db_connector
    
    def set_db_file_name(self, db_file_name):
        self.connection = None
        self.db_connector.set_db_file_name(db_file_name)
        self.get_connection()

    def set_db_connector(self, db_connector):
        self.db_connector = db_connector
        self.connection = None

    def remove_connection(self):
        self.connection = None

    def get_connection(self):
        if self.connection == None:
            try:
                self.connection = self.db_connector.create_connection()
                if self.exclusive_lock:
                    self.begin_exclusive()
            except sqlite3.Error as sqlExp:
                print("DBExecuteSQL.get_connection", "An error occurred:" + sqlExp.args[0])
                raise
        return self.connection

    def begin_exclusive(self):
        self.execute_sql_command("BEGIN EXCLUSIVE; ")

    def get_database_name(self):
        sql_data = self.execute_sql_select("SELECT file FROM pragma_database_list")
        return sql_data[0][0].split("\\")[-1]

    def execute_sql_command(self, sql_command):
        try:
            execute_cursor = self.get_connection().cursor()
            execute_cursor.execute(sql_command)
            execute_cursor.close()
        except sqlite3.Error as sqlExp:
            print("DBExecuteSQL.execute_sql_command", "An error occurred:" + sqlExp.args[0])
            print("DBExecuteSQL.execute_sql_command", "With command:" + sql_command)
            raise
        except Exception as e:
            print("DBExecuteSQL.execute_sql_command", "With command:" + sql_command)
            raise
        except:
            print("DBExecuteSQL.execute_sql_command", "With command:" + sql_command)
            raise
        self.get_connection().commit()

    def insert_data(self, sql_command, data_rows):
        sql_data = None
        insert_data_cursor = self.get_connection().cursor()
        try:
            insert_data_cursor.executemany(sql_command, data_rows)
            insert_data_cursor.execute("SELECT last_insert_rowid()")
            sql_data = insert_data_cursor.fetchall()
        except sqlite3.Error as sqlExp:
            print("DBExecuteSQL.insert_data", "An error occurred:" + sqlExp.args[0])
            print(sql_command)
            if len(data_rows) > 0:
                print(data_rows)
            raise
        insert_data_cursor.close()
        self.get_connection().commit()
        return sql_data

    def execute_sql_select(self, select_command):
        sql_data = []
        try:
            select_cursor = self.get_connection().cursor()
            select_cursor.execute(select_command)
            sql_data = select_cursor.fetchall()
        except sqlite3.Error as sqlExp:
            print("DBExecuteSQL.execute_sql_select", "An error occurred:" + sqlExp.args[0])
            print("DBExecuteSQL.execute_sql_select", "With command:" + select_command)
            raise
        select_cursor.close()
        return sql_data

    def prepare_batch_select(self, select_command):
        select_cursor = None
        try:
            select_cursor = self.get_connection().cursor()
            select_cursor.execute(select_command)
        except sqlite3.Error as sqlExp:
            print("DBExecuteSQL.prepare_batch_select", "An error occurred:" + sqlExp.args[0])
            print("DBExecuteSQL.prepare_batch_select", "With command:" + select_command)
            raise
        return select_cursor

    def select_batch_fetch(self, select_cursor, batch_size=batch_size):
        sql_data = []
        try:
            sql_data = select_cursor.fetchmany(batch_size)
        except sqlite3.Error as sqlExp:
            print("DBExecuteSQL.select_batch_fetch", "An error occurred:" + sqlExp.args[0])
            raise
        return sql_data

    def execute_sql_insert_select(self, select_command):
        sql_data = []
        try:
            select_cursor = self.get_connection().cursor()
            select_cursor.execute(select_command)
            select_cursor.execute("SELECT last_insert_rowid()")
            sql_data = select_cursor.fetchall()
        except sqlite3.Error as sqlExp:
            print("DBExecuteSQL.execute_sql_select", "An error occurred:" + sqlExp.args[0])
            print("DBExecuteSQL.execute_sql_select", "With command:" + select_command)
            raise
        select_cursor.close()
        return sql_data


    def get_list_of_tables(self):
        return self.execute_sql_select("SELECT name FROM sqlite_master WHERE type='table';")

    def switch_to_in_memory(self):
        self.db_connector.set_in_memory()
        self.connection = None

def main():
    db_executeSQl = DBExecuteSQL()
    db_connection = DBConnection()
    db_connection.set_db_file_name("Test.db")
    db_executeSQl.set_db_connector(db_connection)
    connection = db_executeSQl.get_connection()
    print(db_executeSQl.get_list_of_tables())

if __name__ == "__main__":
    main()