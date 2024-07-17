from utility.ListUtility import ListUtility
from class_structure.Structure import Structure
from class_structure.File import File
from class_structure.Package import Package
from class_structure.AmendmentType import *

class StructureWithPackages(Structure):

    def __init__(self, name, primary_key=0):
        super().__init__(name, primary_key)
        self.active = True
        self.packages = []

    def is_active(self):
        return self.active

    def add_package(self, package):
        self.packages.append(package)

    def get_number_of_packages(self):
        return sum(1 for package in self.packages if package.is_active())

    def get_package(self, path):
        if "." in path:
            package_name = File.get_package_name(path)
        else:
            package_name = path
        return ListUtility.find_in_list_by_name(self.packages, package_name)

    def get_package_and_create(self, path, repository):
        package = self.get_package(path)
        if package is None:
            package = Package(File.get_package_name(path), added, repository)
            self.add_package(package)
        return package

    def get_file(self, path):
        file = None
        package = self.get_package(path)
        if package is not None:
            file = package.get_file(path)
            if file is not None and file.package is None:
                file.set_package(package)
        return file

    def get_repository(self):
        return self

    def add_file(self, file):
        package = self.get_package_and_create(file.get_name(), self.get_repository())
        file.set_package(package)
        temp_file = ListUtility.find_in_list_by_name(package.files, file.get_name())
        if temp_file is not None:
            package.files.remove(temp_file)
            file.file_id = temp_file.file_id
            package.files.append(file)
        else:
            package.add_file(file)
