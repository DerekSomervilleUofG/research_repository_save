from repository_save.population_mapping.PopulateStructure import PopulateStructure
from utility.UtilityText import UtilityText

class PopulateDeveloper(PopulateStructure):

    created = False
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PopulateDeveloper, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.developer_id = 0
        self.name = 1
        self.table_name = "developer"
        self.all_columns = "developer_id, name, email, login"
        self.primary_key = "developer_id"

        if not self.created:
            self.sql_rows = []
            self.list_structures = []
            self.counter = 0
        self.created = True

    def select_developer(self, name, repository_id):
        select_statement = self.generate_select_record_by_repository(repository_id)
        select_statement += " AND name = '" + UtilityText.formate_text(name) + "'"
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data

    def select_developer_name_by_repsoitory(self, repository_id):
        select_statement = " SELECT name FROM developer where "
        select_statement += " repository_id = " + str(repository_id)
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data

    def select_developer_name(self):
        select_statement = " SELECT name FROM developer"
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data

    def select_developer_name_and_id(self):
        select_statement = " SELECT developer_id, name FROM developer"
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data    

    def generate_sql_list(self, developers, repository_id):
        sql_data = []
        for developer in developers:
            sql_data.append([developer.name, repository_id])
        return sql_data

    def create_developers(self, developers, repository_id):
        developer_id = self.insert_with_data(self.generate_sql_list(developers, repository_id))
        developer_dict = {}
        self.populate_structure_id(developers, developer_id, developer_dict)

    def get_developer(self, developer, repository_id):
        sql_data = self.select_developer(developer.get_name(), repository_id)
        if len(sql_data) == 0:
            sql_data = self.insert_record_with_foreign_key(developer, repository_id)
        return sql_data[0][0]

    def generate_row(self, developer):
        return ["'" + UtilityText.formate_text(developer.get_name()) + "'",  "'" + developer.get_email() + "'", "'" + UtilityText.formate_text(developer.get_login()) + "'"  ]
