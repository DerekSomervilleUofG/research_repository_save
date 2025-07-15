from utility.UtilityText import UtilityText

class PopulateTable:

    batch_size = 1000

    def __init__(self, db_execute_sql):
        self.db_execute_sql = db_execute_sql
        self.sql_rows = []
        self.list_structures = []

        self.table_name = "table_name"
        self.all_columns = ""
        self.primary_key = "primary_key"
        self.foreign_key = ""
        self.counter = 0
        self.has_next = True
        self.include_primary_key_in_insert = True

    def set_db_execute_sql(self, db_execute_sql):
        self.db_execute_sql = db_execute_sql

    def get_insert_columns(self):
        if self.include_primary_key_in_insert and self.primary_key is not None and self.primary_key != "":
            columns = self.all_columns.replace(self.primary_key + ",","")
        else:
            columns = self.all_columns
        return columns

    def generate_insert_values(self, columns):
        insert_values = " VALUES ( "
        for counter in range(len(columns.split(","))):
            if counter == 0:
                insert_values += "?"
            else:
                insert_values += ", ?"
        insert_values += " ) "
        return insert_values

    def generate_insert_table_columns(self, table, columns):
        insert_statement = "INSERT INTO " + table
        insert_statement += " ( " + columns + " ) "
        return insert_statement

    def generate_insert_with_data(self, table, columns):
        insert_statement = self.generate_insert_table_columns(table, columns)
        insert_statement += self.generate_insert_values( columns)
        return insert_statement

    def insert_with_data(self, data):
        sql_data = self.db_execute_sql.insert_data(self.generate_insert_with_data(self.table_name, self.get_insert_columns()), data)
        return sql_data[0][0]

    def insert_with_data_with_fk(self, data, fk_id):
        data = self.add_foreign_key_id(fk_id, data)
        sql_data = self.db_execute_sql.insert_data(self.generate_insert_with_data(self.table_name, self.get_insert_columns()), data)
        return sql_data[0][0]

    def add_foreign_key_id(self, fk_id, structure_data):
        sql_data = []
        for structure in structure_data:
            structure_list = list(structure)
            structure_list.append(fk_id)
            sql_data.append(structure_list)
        return sql_data

    def generate_mapping(self, structure):
        insert_statement = "ADD MAPPING"
        return insert_statement

    def generate_insert_record(self, table, columns, structure):
        insert_statement = self.generate_insert_table_columns(table, columns)
        insert_statement += " VALUES ( "
        insert_statement += self.generate_mapping(structure)
        insert_statement += " )"
        return insert_statement

    def generate_insert_record_with_foreign_key(self, table, columns, structure, fk_id):
        insert_statement = self.generate_insert_table_columns(table, columns)
        insert_statement += " VALUES ( "
        insert_statement += self.generate_mapping(structure)
        insert_statement += ", " + str(fk_id)
        insert_statement += " )"
        return insert_statement

    def insert_record(self, structure):
        sql_data = self.db_execute_sql.execute_sql_insert_select(self.generate_insert_record(self.table_name, self.get_insert_columns(), structure))
        return sql_data[0][0]

    def insert_record_with_foreign_key(self, structure, fk_id):
        sql_data =  self.db_execute_sql.execute_sql_insert_select(self.generate_insert_record_with_foreign_key(self.table_name, self.get_insert_columns(), structure, fk_id))
        return sql_data[0][0]

    def generate_select_record(self, table_name, columns):
        select_statement = "SELECT " + columns
        select_statement += " FROM " + table_name
        return select_statement

    def select_record(self):
        sql_data = self.db_execute_sql.execute_sql_select(self.generate_select_record(self.table_name, self.all_columns))
        return sql_data
    
    def prepare_batch_select(self):
        return self.db_execute_sql.prepare_batch_select(self.generate_select_record(self.table_name, self.all_columns))

    def prepare_batch_select(self, select):
        return self.db_execute_sql.prepare_batch_select(select)
    
    def next_batch_select(self, select_cursor, batch_size=batch_size):
        sql_data = self.db_execute_sql.select_batch_fetch(select_cursor, batch_size)
        if len(sql_data) < batch_size:
            self.has_next = False
        return sql_data

    def generate_select_record_by_foreign_key(self, table_name, all_columns, fk_id, foreign_key):
        select_statement = self.generate_select_record(table_name, all_columns)
        select_statement += " WHERE " + foreign_key + " in (" + str(fk_id) + ")"
        return select_statement

    def generate_select_record_by_name(self, name):
        select_statement = self.generate_select_record(self.table_name, self.all_columns)
        select_statement += " WHERE name = '" + UtilityText.formate_text(name) + "'"
        return select_statement

    def generate_select_record_by_foreign_key_and_name(self, fk_id, foreign_key, name):
        select_statement = self.generate_select_record_by_foreign_key(self.table_name, self.all_columns, fk_id, foreign_key)
        select_statement += " AND name = '" + UtilityText.formate_text(name) + "'"
        return select_statement

    def select_record_by_repository(self, repository_id):
        sql_data = self.db_execute_sql.execute_sql_select(self.generate_select_record_by_foreign_key(self.table_name, self.all_columns, repository_id, "repository_id"))
        return sql_data

    def select_record_by_name(self, name):
        sql_data = self.db_execute_sql.execute_sql_select(self.generate_select_record_by_name(name))
        return sql_data

    def select_record_id_by_name(self, name):
        sql_data = self.db_execute_sql.execute_sql_select(self.generate_select_record_by_name(name))
        if len(sql_data) > 0:
            record_id = sql_data[0][0]
        else:
            record_id = 0
        return

    def get_record_id(self, structure):
        record_id = self.select_record_id_by_name(structure.get_name())
        if record_id == 0:
            record_id = self.insert_record(structure)
        return record_id

    def select_record_by_repository_and_name(self, repository_id, name):
        sql_data = self.db_execute_sql.execute_sql_select(self.generate_select_record_by_foreign_key_and_name(repository_id, "repository_id", name))
        return sql_data

    def select_record_by_foreign_key_and_name(self, fk_id, name):
        sql_data = self.db_execute_sql.execute_sql_select(self.generate_select_record_by_foreign_key_and_name(fk_id, self.foreign_key, name))
        return sql_data

    def select_record_by_foreign_key(self, fk_id):
        sql_data = self.db_execute_sql.execute_sql_select(self.generate_select_record_by_foreign_key(self.table_name, self.all_columns, fk_id, self.foreign_key))
        return sql_data

    def add_structure(self, new_structure):
        existing_structure = next(iter(structure for structure in self.list_structures if structure == new_structure), None)
        if existing_structure is None:
            self.list_structures.append(new_structure)

    def add_row(self, row):
        self.sql_rows.append(row)

    def generate_row(self, structure):
        return [structure.get_name()]

    def get_structure_rows(self):
        for structure in self.list_structures:
            if structure.is_active() and structure.get_primary_key() == 0:
                self.sql_rows.append(self.generate_row(structure))

    def save_rows(self):
        latest_id = 0
        self.get_structure_rows()
        if len(self.sql_rows) > 0:
            latest_id = self.insert_with_data(self.sql_rows)
        self.sql_rows = []
        self.counter = 0
        return latest_id
    
    def convert_if_string(self, column_value):
        if isinstance(column_value, str):
            column_value = "'" + column_value + "'"
        else:
            column_value = str(column_value)
        return column_value
    
    def generate_update_of_column(self, column_name, column_value):
        column_value = self.convert_if_string(column_value)
        return " " + column_name + " = " + column_value + " "
    
    def generate_update_of_columns(self, row, columns, values):
        update_statement = "UPDATE " + self.table_name + " SET"
        column_statement = ""
        for counter in range(len(columns)):
            if column_statement != "":
                column_statement += ","
            column_statement += self.generate_update_of_column(columns[counter], row[values[counter]])
        update_statement += column_statement
        update_statement += "WHERE " + self.primary_key + " = " + self.convert_if_string(row[0]) + ";\n"
        return update_statement
    
    def generate_update_statement(self, sql_rows, columns, values):
        sql_update_statement = ""
        for row in sql_rows:
            sql_update_statement += self.generate_update_of_columns(row, columns, values)    
        return sql_update_statement
    
    def update_rows(self, columns, values):
        self.get_structure_rows()
        sql_data = self.db_execute_sql.execute_sql_command(self.generate_update_statement(self.sql_rows))
        self.sql_rows = []
        self.counter = 0
