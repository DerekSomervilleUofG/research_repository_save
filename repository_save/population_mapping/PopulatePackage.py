from repository_save.population_mapping.PopulateStructure import PopulateStructure

class PopulatePackage(PopulateStructure):

    _instance = None
    created = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PopulatePackage, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.package_id = 0
        self.name = 1
        self.repository_id = 2

        self.table_name = "package"
        self.all_columns = "package_id, name, repository_id"
        self.primary_key = "package_id"
        self.foreign_key = "repository_id"

        self.primary_key_col = 0
        self.name_col = 1
        self.foreign_key_col = 2
        if not self.created:
            self.sql_rows = []
            self.list_structures = []
            self.counter = 0
        self.created = True

    def update_package_is_active(self, package_id, is_active=0):
        update_statement = "UPDATE package SET is_active = " + str(is_active) + " WHERE package_id = " + str(package_id)
        self.db_execute_sql.execute_sql_command(update_statement)

    def generate_row(self, package):
        return [package.get_name(), package.repository.repository_id]