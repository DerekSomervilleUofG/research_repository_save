from unittest import TestCase
from repository_save.class_structure.DeveloperCommit import DeveloperCommit
from repository_save.population_mapping.PopulateDeveloperCommit import PopulateDeveloperCommit
from repository_save.data_source.DBExecuteSQL import DBExecuteSQL

class TestPopulateDeveloperCommit(TestCase):
    
    developer_commit = DeveloperCommit("123", "derek", "20251001", "message", None, None)
    populate_developer_commit = PopulateDeveloperCommit(DBExecuteSQL())

    def test_get_insert_columns(self):
        self.assertEqual("commit_id, authored_date, repository_id, developer_id", self.populate_developer_commit.get_insert_columns())