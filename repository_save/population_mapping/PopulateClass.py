from repository_save.population_mapping.PopulateStructure import PopulateStructure
from utility.UtilityText import UtilityText
from repository_save.population_mapping.PopulateMethod import PopulateMethod

class PopulateClass(PopulateStructure):

    created = False

    def __init__(self, db_execute_sql):
        super().__init__(db_execute_sql)
        self.table_name = "class"
        self.all_columns = "class_id, name, file_id"
        self.primary_key = "class_id"
        self.foreign_key = "file_id"

        self.primary_key_col = 0
        self.name_col = 1
        self.foreign_key_col = 2

        if not self.created:
            self.sql_rows = []
            self.list_structures = []
            self.counter = 0
        self.created = True

    def generate_mapping(self, class_used):
        insert_statement = "'" + UtilityText.formate_text.formate_text(class_used.get_name()) + "' "
        return insert_statement

    def update_class_is_active(self, class_id, is_active=0):
        update_statement = "UPDATE class SET is_active = " + str(is_active) + " WHERE class_id = " + str(class_id)
        self.db_execute_sql.execute_sql_command(update_statement)

    def get_select_columns(self):
        return "SELECT class_id, name, file_id FROM class  WHERE "

    def select_class_by_name(self, name, file_id=0):
        select_statement = self.get_select_columns()
        select_statement += " name = '" + UtilityText.formate_text(name) + "'"
        select_statement += " and file_id = " + str(file_id)
        sql_data = self.db_execute_sql.execute_sql_select(select_statement)
        return sql_data

    def select_class_id_by_name(self, name, file_id=0):
        class_id = 0
        sql_data = self.select_class_by_name(name, file_id)
        if sql_data is not None and len(sql_data)>0:
            class_id = sql_data[0][0]
        return class_id

    def get_method_data(self, class_used):
        method_data = []
        methods_require_id = []
        for method in class_used.methods:
            if method.get_method_id() == 0:
                method_data.append([UtilityText.formate_text(method.get_name()), class_used.class_id])
                methods_require_id.append(method)
        return method_data, methods_require_id

    def get_commit_method_data(self, class_used, commit_id):
        commit_method_data = []
        for method in class_used.methods:
            commit_method_row = []
            commit_method_row.append(UtilityText.formate_text(method.get_name()))
            commit_method_row.append(method.code_change_statistic.lines_added)
            commit_method_row.append(method.code_change_statistic.lines_changed)
            commit_method_row.append(method.code_change_statistic.lines_removed)
            commit_method_row.append(method.code_change_statistic.lines_same)
            commit_method_row.append(method.code_change_statistic.lines_similar)
            commit_method_row.append(method.amendment)
            commit_method_row.append(method.get_method_id())
            commit_method_row.append(class_used.class_id)
            commit_method_row.append(commit_id)
            commit_method_data.append(commit_method_row)
        return commit_method_data

    def get_prior_method_data(self, class_used, commit_id, prior_knowledge_id):
        prior_method_data = []
        for method in class_used.methods:
            prior_method_row = []
            prior_method_row.append(UtilityText.formate_text(method.get_name()))
            prior_method_row.append(method.get_method_id())
            prior_method_row.append(class_used.class_id)
            prior_method_row.append(commit_id)
            prior_method_row.append(prior_knowledge_id)
            prior_method_data.append(prior_method_row)
        return prior_method_data

    def get_class_by_name(self, class_used, file_id):
        sql_data = self.select_record_by_foreign_key_and_name(file_id, class_used.get_name())
        if len(sql_data) > 0:
            class_id = sql_data[0][0]
        else:
            class_id = self.insert_record_with_foreign_key(class_used, file_id)
        class_used.set_class_id(class_id)
        return class_id

    def generate_row(self, class_used):
        return [class_used.get_name(), class_used.owned_by_file.get_file_id()]
