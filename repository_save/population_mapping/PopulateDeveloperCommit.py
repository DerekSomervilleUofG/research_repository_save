from repository_save.population_mapping.PopulateDeveloper import PopulateDeveloper
from utility.UtilityText import UtilityText
from utility.ListUtility import ListUtility
from repository_save.population_mapping.PopulateStructureIndividual import PopulateStructureIndividual

class PopulateDeveloperCommit(PopulateStructureIndividual):

    created = False

    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.commit_id = 0
        self.authored_date = 1
        self.repository_id = 2
        self.developer_id = 3
        self.table_name = "developer_commit"
        self.all_columns = "commit_id, authored_date, repository_id, developer_id"
        self.primary_key = ""  # We save with the commit_id
        self.foreign_key = "repository_id"
        if not self.created:
            self.sql_rows = []
            self.list_structures = []
            self.counter = 0
        self.created = True

    def generate_developer_commit_data(self, developer_commits):
        commit_data = []
        for commit in developer_commits:
            commit_data.append([commit.get_name(), commit.date, commit.repository.repository_id, commit.developer.developer_id])
        return commit_data

    def update_developer_commit_repo_count(self, developer_commit, repository):
        update_statement = "UPDATE developer_commit set number_of_repo_packages = " + str(repository.get_number_of_packages())
        update_statement += ", number_of_repo_files = " + str(repository.get_number_of_files())
        update_statement += ", number_of_repo_classes = " + str(repository.get_number_of_classes())
        update_statement += ", number_of_repo_methods = " + str(repository.get_number_of_methods())
        update_statement += " WHERE commit_id = '" + developer_commit.get_name() + "'"
        self.db_execute_sql.execute_sql_command(update_statement)


    def select_developer_commits(self, repository_id):
        select_statement = self.generate_select_record_by_foreign_key(self.table_name, self.all_columns, repository_id, "repository_id")
        select_statement += " order by developer_id, authored_date asc"
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data

    def select_commit_and_repo_count(self, repository_id):
        select_statement = "SELECT dc.commit_id, dc.authored_date "
        select_statement += ", dc.number_of_repo_packages, dc.number_of_repo_files, dc.number_of_repo_classes, dc.number_of_repo_methods "
        select_statement += " FROM developer_commit dc "
        select_statement += " where repository_id = " + str(repository_id)
        select_statement += " order by dc.developer_id, dc.authored_date asc"
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data

    def select_commit_size (self, repository_id):
        select_statement = "select dc.commit_id, count(distinct(cf.package_id)), count(cf.file_id), count(cc.class_id), count(cm.method_id) "
        select_statement += "from developer_commit dc, commit_file cf "
        select_statement += "left outer join commit_class cc on "
        select_statement += " cc.commit_id = cf.commit_id and "
        select_statement += " cc.file_id = cf.file_id "
        select_statement += " left outer join commit_method cm on "
        select_statement += " cm.commit_id = cc.commit_id and "
        select_statement += " cm.class_id = cc.class_id "
        select_statement += " where dc.commit_id = cf.commit_id "
        select_statement += " and dc.repository_id = " + str(repository_id)
        select_statement += " group by dc.commit_id "
        select_statement += " order by dc.developer_id, dc.authored_date asc "
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data

    def select_prior_knowledge(self, repository_id):
        select_statement = "select dc.commit_id, count(distinct(pf.package_id)), count(pf.file_id), count(pc.class_id), count(pm.method_id) "
        select_statement += "from developer_commit dc, prior_file pf "
        select_statement += "left outer join prior_class pc on "
        select_statement += " pc.commit_id = pf.commit_id and "
        select_statement += " pc.file_id = pf.file_id "
        select_statement += " left outer join prior_method pm on "
        select_statement += " pm.commit_id = pc.commit_id and "
        select_statement += " pm.class_id = pc.class_id "
        select_statement += " where dc.commit_id = pf.commit_id "
        select_statement += " and dc.repository_id = " + str(repository_id)
        select_statement += " group by dc.commit_id "
        select_statement += " order by dc.developer_id, dc.authored_date asc "
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data

    def delete_developer_commit(self, repository_id):
        delete_statement = " DELETE FROM developer_commit WHERE repository_id = " + str(repository_id)
        self.db_execute_sql.execute_sql_command(delete_statement)

    def generate_row(self, developer_commit):
        return [UtilityText.formate_text(developer_commit.get_name()), UtilityText.formate_text(developer_commit.get_author_date()), str(developer_commit.repository.get_repository_id()), str(developer_commit.developer.get_primary_key())]
    
