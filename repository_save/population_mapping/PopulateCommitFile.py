from utility.UtilityText import UtilityText
from repository_save.population_mapping.PopulateCommit import PopulateCommit

class PopulateCommitFile(PopulateCommit):

    sql_name = 0
    sql_file_id = 1
    sql_package_id = 2
    sql_repository_id = 3
    sql_commit_id = 4
    sql_developer_id = 5

    def __init__(self):

        self.table_name = "commit_file"
        self.all_columns = "name, lines_added, lines_changed, lines_removed, lines_same, lines_similar, amendment_type, file_id, commit_id, package_id, repository_id"
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
            cls._instance = super(PopulateCommitFile, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance


    def insert_commit_file(self, file, package_id, commit_id, repository_id):
        if commit_id is None:
            commit_id = 0
        if repository_id is None:
            repository_id = 0
        code_change_statistic = file.code_change_statistic
        insert_statement = "INSERT INTO commit_file (name, lines_added, lines_changed, lines_removed, lines_same, lines_similar, amendment_type, file_id, commit_id, package_id, repository_id) values ("
        insert_statement += "'" + UtilityText.formate_text(file.get_name()) + "', "
        insert_statement += str(code_change_statistic.lines_added) + ", "
        insert_statement += str(code_change_statistic.lines_changed) + ", "
        insert_statement += str(code_change_statistic.lines_removed) + ", "
        insert_statement += str(code_change_statistic.lines_same) + ", "
        insert_statement += str(code_change_statistic.lines_similar) + ", "
        insert_statement += "'" + file.amendment + "', "
        insert_statement += str(file.file_id) + ", "
        insert_statement += "'" + str(commit_id) + "',"
        insert_statement += str(package_id) + ", "
        insert_statement += str(repository_id) + ")"
        self.db_execute_sql.execute_sql_command(insert_statement)

    def get_select_columns(self):
        return "select cf.name, cf.file_id, cf.package_id, cf.repository_id, cf.commit_id, developer_id"

    def select_commit_file(self, repository_id):
        select_statement = self.get_select_columns()
        select_statement += " from commit_file cf, developer_commit dc "
        select_statement += " where cf.repository_id = " + str(repository_id)
        select_statement += " and dc.commit_id = cf.commit_id "
        select_statement += " order by developer_id, commit_file_id asc "
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data

    def generate_row(self, file):
        row = super().generate_row(file)
        row.append(file.get_file_id())
        row.append(file.developer_commit.get_name())
        row.append(file.package.get_package_id())
        row.append(file.package.repository.get_repository_id())
        return row