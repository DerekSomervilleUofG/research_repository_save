import sqlite3, os, shutil

class DBConnection():

    db_file_prefix = "resource/"
    db_file_template = "template.tmplt"
    db_file_name = db_file_template
    in_memory_database = ":memory:"
    sql_lite_url = db_file_prefix + db_file_name

    def set_db_file_name(self, db_file_name):
        self.db_file_name = db_file_name
        self.create_database(self.determine_database_name(db_file_name))
        self.create_connection()

    def determine_database_name(self, db_file_name):
        if "/" in db_file_name or "\\" in db_file_name:
            self.sql_lite_url = db_file_name
        else:
            self.sql_lite_url = self.db_file_prefix + db_file_name
        return self.sql_lite_url

    def create_database(self, sql_lite_url):
        if not os.path.exists(sql_lite_url):
            print("create_database", "missing", sql_lite_url)
            shutil.copyfile(self.db_file_prefix + self.db_file_template, sql_lite_url)

    def set_in_memory(self):
        self.sql_lite_url = self.in_memory_database

    def create_connection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.sql_lite_url)
        except sqlite3.Error as sqlExp:
            self.log_message("DBConnection.create_connection", "An error occurred:" + sqlExp.args[0], "")
        return connection

def main():
    connection = DBConnection()
    connection.create_connection()

if __name__ == "__main__":
    main()