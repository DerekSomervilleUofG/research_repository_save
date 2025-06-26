from unittest import TestCase
from repository_save.population_mapping.PopulateCommitKnownPackageNumber import PopulateCommitKnownPackageNumber
from repository_save.class_structure.CommitKnownPackageNumber import CommitKnownPackageNumber
from repository_save.population_mapping.ControlPopulate import ControlPopulate

class test_PopulateCommitKnownPackageNumber(TestCase):

    control_populate = ControlPopulate()
    populate_commit_known_package_number = PopulateCommitKnownPackageNumber(control_populate.db_execute_sql)
    commit_known_package_number = CommitKnownPackageNumber("COMMIT123", 3, 2, 1, 1)

    def test_generate(self):
        self.assertEqual(["COMMIT123", 2, 3 , 1, 1], self.populate_commit_known_package_number.generate_row(self.commit_known_package_number))

    def test_add_structure(self):
        self.populate_commit_known_package_number.add_structure(self.commit_known_package_number)
        self.assertEqual(1, len(self.populate_commit_known_package_number.list_structures))

    def test_save_rows(self):
        self.control_populate.db_execute_sql.set_db_file_name("resource/database/test.db")
        self.populate_commit_known_package_number.add_structure(self.commit_known_package_number)
        self.populate_commit_known_package_number.save_rows()
        self.assertEqual(0, len(self.populate_commit_known_package_number.list_structures))

    def test_database_name(self):
        self.control_populate.db_execute_sql.set_db_file_name("resource/database/codebase.db")
        self.assertEqual("codebase.db", self.control_populate.db_execute_sql.get_database_name())