from class_structure.StructureWithPackages import StructureWithPackages
from class_structure.File import File
from class_structure.AmendmentType import *

import copy

class DeveloperCommit(StructureWithPackages):

    def __init__(self, name, # The `author`, `date`, `message`, `repository`, and `developer`
    # parameters in the `DeveloperCommit` class constructor are used to
    # initialize the attributes of a developer commit object. Here is a
    # breakdown of what each parameter represents:
    # The `author`, `date`, `message`, `repository`, and `developer`
    # parameters in the `DeveloperCommit` class constructor are used to
    # initialize the attributes of a developer commit object. Here is a
    # breakdown of what each parameter represents:
    author, date, message, repository, developer):
        super().__init__(name)
        self.author = author
        self.date = date
        self.message = message
        self.repository = repository
        self.developer = developer

    def clear(self):
        for package in self.packages:
            package.clear()
            del package
        self.packages = []

    def remove_lines(self):
        for package in self.packages:
            package.remove_lines()

    def get_author_name(self):
        return self.author

    def get_name(self):
        return self.name

    def get_message_first_line(self):
        first_line = self.message.split("\n")[0]
        first_line = first_line.replace(", ", ";")
        first_line = first_line.replace("\n", "").strip()
        return first_line

    def get_author_date(self):
        return self.date

    def get_message(self):
        return self.message

    def set_commits(self, previous_commit, current_commit):
        self.previous_commit = copy.copy(previous_commit)
        self.current_commit = copy.copy(current_commit)

    def get_file(self, path):
        file = super().get_file(path)
        if file is None:
            repo_file = self.repository.get_file(path)
            if repo_file is not None:
                file = copy.copy(repo_file)
                file.set_repo_file(repo_file)
                file.classes_used = []
        return file

    def add_file(self, file):
        temp_file = super().get_file(file.get_name())
        if temp_file is None:
            file.set_developer_commit(self)
            super().add_file(file)

    def get_package(self, path):
        package = super().get_package(path)
        if package is None:
            repo_package = self.repository.get_package(path)
            if package is not None:
                package = copy.copy(repo_package)
                package.set_repo_package(repo_package)
                package.files = []
        return package

    def add_file_by_name(self, path):
        package = self.get_package_and_create(path, self.repository)
        file = File(path, added, package=package)
        self.add_file(file)
        return file

    def get_repository(self):
        return self.repository

    def to_string(self, spacer="\n", display_class_name=True):
        display = ""
        if display_class_name:
            display += self.get_class_name() + spacer
        display += self.get_name() + spacer + self.get_author_name() + spacer + self.get_author_date()
        return display
