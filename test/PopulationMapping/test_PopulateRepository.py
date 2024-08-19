from repository_save.population_mapping.PopulateRepository import PopulateRepository
from repository_save.data_source.DBExecuteSQL import DBExecuteSQL
from class_structure.Repository import Repository
from unittest import TestCase

class TestPopulateRepository(TestCase):
    
    db_execute_sql = DBExecuteSQL()
    populate_repository = PopulateRepository(db_execute_sql)
    repository_name = "https://stgit.dcs.gla.ac.uk/DerekSomerville/database_batch_save.git"
    repository = Repository(repository_name)

    def test_generate_insert_values(self):
        columns = "repository_id, name, url"
        self.assertEqual(" VALUES ( ?, ?, ? ) ", self.populate_repository.generate_insert_values(columns))

    def test_generate_insert_values_one_column(self):
        columns = "repository_id"
        self.assertEqual(" VALUES ( ? ) ", self.populate_repository.generate_insert_values(columns))

    def test_generate_insert_with_data(self):
        table = "repository"
        columns = "repository_id"
        self.assertEqual("INSERT INTO repository ( repository_id )  VALUES ( ? ) ", self.populate_repository.generate_insert_with_data(table, columns))

    def test_generate_insert_record(self):
        self.assertEqual("INSERT INTO repository ( repository_id )  VALUES ( 'database_batch_save', 'https://stgit.dcs.gla.ac.uk/DerekSomerville/database_batch_save.git' )", self.populate_repository.generate_insert_record("repository", "repository_id", self.repository))

    def test_generate_select_record(self):
        self.assertEqual("SELECT repository_id FROM repository", self.populate_repository.generate_select_record("repository", "repository_id"))

    def test_generate_row(self):
        self.assertEqual( ["database_batch_save", self.repository_name], self.populate_repository.generate_row(self.repository))