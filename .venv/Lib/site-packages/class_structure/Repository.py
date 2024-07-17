from utility.ListUtility import ListUtility
from class_structure.Package import Package
from class_structure.Structure import Structure
from class_structure.File import File
from class_structure.ClassStructure import ClassStructure
from class_structure.StructureWithPackages import StructureWithPackages

class Repository(StructureWithPackages):

    def __init__(self, repo_path, primary_key=0):
        super().__init__(self.determine_repo_name(repo_path), primary_key)
        self.repo_path = repo_path
        self.in_database = False
        self.entry_database = False
        self.packages = []
        self.developers = []
        self.commits = []


    def determine_repo_name(self, repo_path):
        return repo_path.split("/")[-1].split(".")[0]

    def get_repository_id(self):
        return self.get_primary_key()

    def set_repository_id(self, repository_id):
        self.set_primary_key(repository_id)

    def get_name(self):
        return self.name

    def get_repo_path(self):
        return self.repo_path

    def add_package(self, package):
        parent_package = ListUtility.find_in_list_by_name(self.packages, package.get_parent_package())
        if parent_package is not None:
            ListUtility.add_to_unique_list(parent_package.packages, package)
        self.packages.append(package)

    def add_developer(self, developer):
        self.developers.append(developer)

    def add_commit(self, commit):
        self.commits.append(commit)

    def get_developers(self):
        developers = ""
        for developer in self.developers:
            developers += developer.to_string() + " , "
        return developers

    def get_files(self):
        files = ""
        for file in self.files:
            files += file.to_string() + " , "
        return files

    def merge_package_code_statistics(self):
        for package in self.packages:
            for file in package.files:
                package.merge_code_change_statistic(file.code_change_statistic)



    def store_a_method_in_the_repostiory(self, added_method, removed_method):
        existing_package = ListUtility.find_in_list_by_name(self.package, added_method.ownedby_file.package.name)
        if existing_package is None:
            existing_package = Package(added_method.ownedby_file.package.name, amendment=Structure.renamed, created_by_commit=self, parent_package=added_method.ownedby_file.package.parent_package)
            self.repository.add_package(existing_package)
        else:
            existing_file = ListUtility.find_in_list_by_name(existing_package.files, added_method.ownedby_file.get_name())
        if existing_file is None:
            existing_file = File(added_method.ownedby_file.get_name(), Structure.renamed)
            existing_package.add_file(existing_file)
        else:
            existing_class = ListUtility.find_in_list_by_name(existing_file.classes_used, added_method.ownedby_class.get_name())
        if existing_class is None:
            existing_class = ClassStructure(added_method.ownedby_class.get_name(), Structure.renamed)
            existing_file.add_class(existing_class)
        existing_method = self.find_a_method_in_the_repostory(removed_method)
        if existing_method is not None:
            existing_class.add_method(existing_method)

    def find_a_method_in_the_repostory(self, removed_method):
        existing_method = None
        existing_package = ListUtility.find_in_list_by_name(self.package, removed_method.ownedby_file.package.name)
        if existing_package is not None:
            existing_file = ListUtility.find_in_list_by_name(existing_package.files, removed_method.ownedby_file.get_name())
        if existing_file is not None:
            existing_class = ListUtility.find_in_list_by_name(existing_file.classes_used, removed_method.ownedby_class.get_name())
        if existing_class is not None:
            existing_method = ListUtility.find_in_list_by_name(existing_class.methods, removed_method.get_name())
        return existing_method

    def merge_repository(self, changed_packages):
        Package.merge_packages(self.packages, changed_packages)

    def to_string(self, spacer="\n"):
        display= ""
        for package in self.packages:
            display += package.to_string(spacer) + spacer
        display += "DEVELOPERS" + spacer
        for developer in self.developers:
            display += developer.to_string() + spacer
        return display
