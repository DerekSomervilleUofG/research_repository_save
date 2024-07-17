from repository_save.population_mapping.PopulateCommit import PopulateCommit
from utility.UtilityText import UtilityText
class PopulateCommitClass(PopulateCommit):

    sql_name = 0
    sql_class_id = 1
    sql_file_id = 2
    sql_commit_id = 3
    sql_developer_id = 4

    def __init__(self):
        self.table_name = "commit_class"
        self.all_columns = "name, lines_added, lines_changed, lines_removed, lines_same, lines_similar, amendment_type, class_id, file_id, commit_id"
        self.primary_key = ""
        if not self.created:
            self.sql_rows = []
            self.list_structures = []
            self.counter = 0
        self.created = True

    created = False
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PopulateCommitClass, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance


    def generate_mapping(self, class_used):
        code_change_statistic = class_used.code_change_statistic
        insert_statement = "'" + UtilityText.formate_text(class_used.get_name()) + "', "
        insert_statement += str(code_change_statistic.lines_added) + ", "
        insert_statement += str(code_change_statistic.lines_changed) + ", "
        insert_statement += str(code_change_statistic.lines_removed) + ", "
        insert_statement += str(code_change_statistic.lines_same) + ", "
        insert_statement += str(code_change_statistic.lines_similar) + ", "
        insert_statement += "'" + class_used.amendment + "', "
        insert_statement += str(class_used.get_class_id()) + ","

    def generate_row(self, class_used):
        row = super().generate_row(class_used)
        row.append(class_used.get_primary_key())
        row.append(class_used.owned_by_file.get_file_id())
        row.append(class_used.owned_by_file.developer_commit.get_name())
        return row

    def generate_insert_record(self, class_used, file_id, commit_id):
        if commit_id is None:
            commit_id = 0
        insert_statement = self.generate_insert_table_columns(self.table_name, self.get_insert_columns())
        insert_statement += " VALUES ( "
        insert_statement += self.generate_mapping(class_used)
        insert_statement += "," + str(file_id)
        insert_statement += ", '" + str(commit_id) + "'"
        insert_statement += " )"

    def get_select_columns(self):
        return "select cc.name, cc.class_id, cc.file_id, cc.commit_id, developer_id"

    def select_commit_class(self, repository_id):
        select_statement = self.get_select_columns()
        select_statement += " from commit_class cc, developer_commit dc "
        select_statement += " where dc.repository_id = " + str(repository_id)
        select_statement += " and dc.commit_id = cc.commit_id "
        select_statement += " order by developer_id, commit_class_id asc "
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data



