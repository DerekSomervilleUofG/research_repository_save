from class_structure.StructureWithCode import StructureWithCode
from utility.ListUtility import ListUtility


class File(StructureWithCode):

    interpreters = []

    def __init__(self, name, amendment, latest = "", package=None, primary_key=0):
        super().__init__(name, amendment, primary_key)
        self.file_methods = []
        self.classes_used = []
        self.libraries = []
        self.package = package
        self.latest = latest
        self.developer_commit = None

    def set_file_id(self, file_id):
        self.set_primary_key(file_id)

    def get_file_id(self):
        return self.get_primary_key()
    
    def set_developer_commit(self, developer_commit):
        self.developer_commit = developer_commit
        
    def get_developer_commit(self):
        return self.developer_commit

    def get_latest(self):
        return self.latest

    def get_package_name(path):
        package_name = ""
        position = path.rfind("/")
        if position > 0 and len(path.split("/")[0]) > 0 :
            package_name = path[0:position]
        return package_name

    def set_package(self, package):
        self.package = package

    def add_class(self, class_used):
        if "ClassStructure" not in class_used.get_class_name():
            self.log_message("add_class", self.get_name() + " " + class_used.get_class_name + " " + class_used.get_name)
            raise
        ListUtility.add_to_unique_list(self.classes_used, class_used)

    def add_file_method(self, file_method):
        ListUtility.add_to_unique_list(self.file_methods, file_method)

    def add_library(self, library):
        ListUtility.add_to_unique_list(self.libraries, library)

    def get_file_type(self):
        return self.name.split(".")[1]

    def to_string(self, spacer="\n", display_class_name=True):
        display = super().to_string(spacer, display_class_name) + " " + self.code_change_statistic.to_string() + spacer
        return display
