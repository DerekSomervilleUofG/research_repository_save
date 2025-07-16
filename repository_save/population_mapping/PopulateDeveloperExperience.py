from repository_save.population_mapping.PopulateStructure import PopulateStructure
from repository_save.data_source.DBExecuteSQL import DBExecuteSQL
from utility.UtilityText import UtilityText
class PopulateDeveloperExperience(PopulateStructure):

    created = False

    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.developer_experience_id = 0
        self.name = 1
        self.repository_id = 2
        self.table_name = "developer_experience"
        self.all_columns = "developer_experience_id, repository_name, language, pull_date, developer_id"
        self.primary_key = "developer_experience_id"

        if not self.created:
            self.sql_rows = []
            self.list_structures = []
            self.counter = 0
        self.created = True

    def generate_row(self, developer_experience):
        return ["'" + UtilityText.formate_text(developer_experience.get_name()) + "'","'" + developer_experience.language + "'",  int(developer_experience.get_pull_date()) , str(developer_experience.developer_id) ]
