from class_structure.StructureWithCode import StructureWithCode
from utility.ListUtility import ListUtility
from class_structure.ClassStructure import ClassStructure
from class_structure.Method import Method
from class_structure.File import File
from class_structure.FileMethod import FileMethod

class Package(StructureWithCode):

    interpreter = None

    def __init__(self, name, amendment, repository=None, parent_package=None, primary_key=0):
        super().__init__(name, amendment, primary_key)
        self.files = []
        self.packages = []
        self.parent_package = parent_package
        self.repository = repository

    def set_package_id(self, package_id):
        self.set_primary_key(package_id)

    def get_package_id(self):
        return self.get_primary_key()

    def get_files(self):
        return self.files

    def add_file(self, file):
        self.files.append(file)

    def add_package(self, package):
        self.packages.append(package)

    def get_parent_package(self):
        parent_package = ""
        position = self.name.rfind("/")
        if position > 0:
            parent_package = self.name[0:position]
        return parent_package

    def to_string(self, spacer="\n", display_class_name=True):
        display = super().to_string(spacer) + " " + self.code_change_statistic.to_string() + spacer
        #for file in self.files:
        #    display += file.to_string(spacer)
        return display

    def merge_repository_file_methods(existing_file, changed_file):
        for changed_file_method in changed_file.file_methods:
            existing_file_method = ListUtility.find_in_list_by_name(existing_file.file_methods, changed_file_method)
            if existing_file_method is None:
                existing_file_method = FileMethod(changed_file_method.get_name(), changed_file_method.amendement)
                ListUtility.add_to_unique_list(existing_file.file_methods, existing_file_method)
            elif not changed_file_method.is_active():
                existing_file.file_methods.remove(existing_file_method)
            changed_file.merge_code_change_statistic(changed_file_method.code_change_statistic)

    def merge_repostiory_classes(existing_file, changed_file):
        for changed_class in changed_file.classes_used:
            existing_class = ListUtility.find_in_list_by_name(existing_file.classes_used, changed_class.get_name())
            if existing_class == None:
                existing_class = ClassStructure(changed_class.get_name(), changed_class.amendment)
                existing_file.classes_used.append(existing_class)

            if changed_class.is_active():
                for changed_method in changed_class.methods:
                    existing_method = ListUtility.find_in_list_by_name(existing_class.methods, changed_method)
                    if existing_method is None:
                        existing_method = Method(changed_method.get_name(), changed_method.amendment)
                        ListUtility.add_to_unique_list(existing_class.methods, existing_method)
                    if not changed_method.is_active():
                        existing_class.methods.remove(existing_method)
                    changed_class.merge_code_change_statistic(changed_method.code_change_statistic)
                changed_file.merge_code_change_statistic(changed_class.code_change_statistic)
            else:
                existing_file.classes_used.remove(existing_class)

    def merge_repository_files(existing_package, changed_package):
        for changed_file in changed_package.files:
            existing_file = ListUtility.find_in_list_by_name(existing_package.files, changed_file.get_name())
            if existing_file == None:
                existing_file = File(changed_file.get_name(), changed_file.amendment)
                existing_package.files.append(existing_file)
            if changed_file.is_active():
                Package.merge_repository_file_methods(existing_file, changed_file)
                Package.merge_repostiory_classes(existing_file, changed_file)
            else:
                existing_package.files.remove(existing_file)
            changed_package.merge_code_change_statistic(changed_file.code_change_statistic)

    def merge_packages(existing_packages, changed_packages):
        for changed_package in changed_packages:
            existing_package = ListUtility.find_in_list_by_name(existing_packages, changed_package.get_name())
            if existing_package is None:
                if changed_package.parent_package is not None:
                    existing_parent_package = ListUtility.find_in_list_by_name(existing_packages, changed_package.parent_package.get_name())
                    if existing_parent_package is None:
                        existing_parent_package = Package(changed_package.get_name(), amendment=Structure.added, parent_package=None)
                else:
                    existing_parent_package = None
                existing_package = Package(changed_package.get_name(), amendment=Structure.added, parent_package=existing_parent_package)
                existing_packages.append(existing_package)
            Package.merge_repository_files(existing_package, changed_package)
            existing_package.merge_code_change_statistic(changed_package.code_change_statistic)

    def copy_packages(packages):
        new_packages = []
        for package in packages:
            if package.is_active():
                new_package = Package(package.get_name(), amendment=package.amendment, parent_package=package.parent_package)
                new_packages.append(new_package)
                for file in package.files:
                    if file.is_active():
                        new_file = File(file.get_name(), file.amendment)
                        new_package.files.append(new_file)
                        for file_method in file.file_methods:
                            if file_method.is_active():
                                new_file_method = FileMethod(file_method.get_name(), file_method.amendment)
                                new_file.file_methods.append(new_file_method)
                        for class_used in file.classes_used:
                            if class_used.is_active():
                                new_class_used = ClassStructure(class_used.get_name(), class_used.amendment)
                                new_file.classes_used.append(new_class_used)
                                for method in class_used.methods:
                                    if method.is_active():
                                        new_method = Method(method.get_name(), method.amendment)
                                        new_class_used.methods.append(new_method)
        return new_packages