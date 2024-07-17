from repository_save.population_mapping.PopulateStructure import PopulateStructure

class PopulateFile(PopulateStructure):

    created = False
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PopulateFile, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.file_id = 0
        self.name = 1
        self.package_id = 2
        self.repository_id = 3
        self.table_name = "file"
        self.all_columns = "file_id, name, package_id, repository_id"
        self.primary_key = "file_id"
        self.foreign_key = "package_id"

        self.primary_key_col = 0
        self.name_col = 1
        self.foreign_key_col = 2

        if not self.created:
            self.sql_rows = []
            self.list_structures = []
            self.counter = 0
        self.created = True

    def update_file_is_active(self, file_id, is_active=0, syntax_error=False):
        update_statement = "UPDATE file SET is_active =  " + str(is_active)
        if syntax_error:
            update_statement += ", syntax_error = 1 "
        update_statement += " WHERE file_id = " + str(file_id)
        self.db_execute_sql.execute_sql_command(update_statement)

    def generate_row(self, file):
        return [file.get_name(), file.package.get_package_id(), file.package.repository.get_repository_id()]

