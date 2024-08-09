from utility.UtilityText import UtilityText
from repository_save.population_mapping.PopulateCommit import PopulateCommit

class PopulateCommitMethod(PopulateCommit):

    sql_name = 0
    sql_method_id = 1
    sql_class_id = 2
    sql_commit_id = 3
    sql_developer_id = 4
    
    created = False

    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.table_name = "commit_method"
        self.all_columns = "name, lines_added, lines_changed, lines_removed, lines_same, lines_similar, amendment_type, method_id, class_id, commit_id"
        self.primary_key = ""

        if not self.created:
            self.sql_rows = []
            self.list_structures = []
            self.counter = 0
        self.created = True

    def insert_commit_method_with_data(self, method_data):
        insert_statement = "INSERT INTO commit_method (name, lines_added, lines_changed, lines_removed, lines_same, lines_similar, amendment_type, method_id, class_id, commit_id) "
        insert_statement += " values (?,?,?,?,?,?,?,?,?,?)"
        sql_data = self.db_execute_sql.insert_data(insert_statement, method_data)
        return sql_data[0][0]

    def insert_commit_method(self, method, class_id, commit_id):
        if commit_id is None:
            commit_id = 0
        code_change_statistic = method.code_change_statistic
        insert_statement = "INSERT INTO commit_method (name, lines_added, lines_changed, lines_removed, lines_same, lines_similar, amendment_type, method_id, class_id, commit_id) values ("
        insert_statement += "'" + UtilityText.formate_text(method.get_name()) + "', "
        insert_statement += str(code_change_statistic.lines_added) + ", "
        insert_statement += str(code_change_statistic.lines_changed) + ", "
        insert_statement += str(code_change_statistic.lines_removed) + ", "
        insert_statement += str(code_change_statistic.lines_same) + ", "
        insert_statement += str(code_change_statistic.lines_similar) + ", "
        insert_statement += "'" + method.amendment + "', "
        insert_statement += str(method.get_method_id()) + ","
        insert_statement += str(class_id) + ","
        insert_statement += "'" + str(commit_id) + "')"
        self.db_execute_sql.execute_sql_command(insert_statement)

    def get_select_columns(self):
        return "select cm.name, cm.method_id, cm.class_id, cm.commit_id, developer_id"

    def select_commit_method(self, repository_id):
        select_statement = self.get_select_columns()
        select_statement += " from commit_method cm, developer_commit dc "
        select_statement += " where dc.repository_id = " + str(repository_id)
        select_statement += " and dc.commit_id = cm.commit_id "
        select_statement += " order by developer_id, commit_method_id asc "
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data

    def generate_row(self, method):
        row = super().generate_row(method)
        row.append(method.get_primary_key())
        row.append(method.owned_by_class.get_primary_key())
        row.append(method.owned_by_class.owned_by_file.developer_commit.get_name())
        return row
