from repository_save.population_mapping.PopulateStructure import PopulateStructure
from utility.UtilityText import UtilityText

class PopulateMethod(PopulateStructure):

    created = False
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PopulateMethod, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.table_name = "method"
        self.all_columns = "method_id, name, class_id"
        self.primary_key = "method_id"
        self.foreign_key = "class_id"

        self.primary_key_col = 0
        self.name_col = 1
        self.foreign_key_col = 2

        if not self.created:
            self.sql_rows = []
            self.list_structures = []
            self.counter = 0
        self.created = True

    def insert_method_with_data(self, method_data):
        insert_statement = "INSERT INTO method (name, class_id) values (?,?)"
        sql_data = self.db_execute_sql.insert_data(insert_statement, method_data)
        return sql_data[0][0]

    def insert_method(self, method, class_id):
        insert_statement = "INSERT INTO method (name, class_id) values ("
        insert_statement += "'" + UtilityText.formate_text(method.get_name()) + "', "
        insert_statement += str(class_id) + ")"
        sql_data = self.db_execute_sql.execute_sql_insert_select(insert_statement)
        return sql_data[0][0]

    def update_method_is_active(self, method_id, is_active=0):
        update_statement = "UPDATE method SET is_active = " + str(is_active) + " WHERE method_id = " + str(method_id)
        self.db_execute_sql.execute_sql_command(update_statement)

    def get_select_columns(self):
        return "SELECT method_id, name, class_id FROM method  WHERE "

    def select_method_by_name(self, name, class_id):
        select_statement = self.get_select_columns()
        select_statement += " name = '" + UtilityText.formate_text(name) + "'"
        select_statement += " and class_id = " + str(class_id)
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data

    def select_method_id_by_name(self, name, class_id):
        method_id = 0
        sql_data = self.select_method_by_name(name, class_id)
        if sql_data is not None and len(sql_data)>0:
            method_id = sql_data[0][0]
        return method_id

    def get_method_by_name(self, method, class_id):
        method_id = self.select_method_id_by_name(method.get_name(), class_id)
        if method_id == 0:
            method_id = self.insert_method(method, class_id)
        return method_id

    def generate_row(self, method):
        return [method.get_name(), method.owned_by_class.get_primary_key()]
