from class_structure.Repository import Repository
from unittest import TestCase

class TestRepository(TestCase):

    url = "https://stgit.dcs.gla.ac.uk/DerekSomerville/database_batch_save.git"
    repository = Repository(url)

    def test_determine_repo_name(self):
        self.assertEqual("database_batch_save", self.repository.determine_repo_name(self.url))

    def test_get_name(self):
        self.assertEqual("database_batch_save", self.repository.get_name())

    def test_default_primary_key(self):
        self.assertEqual(0, self.repository.get_primary_key())

    def test_default_repository_key(self):
        self.assertEqual(0, self.repository.get_repository_id())

    def test_get_repo_path(self):
        self.assertEqual(self.url, self.repository.get_repo_path())

    def test_set_repository_id(self):
        self.repository.set_repository_id(1)
        self.assertEqual(1, self.repository.get_repository_id())

    def test_set_repository_id_primary_key(self):
        self.repository.set_repository_id(1)
        self.assertEqual(1, self.repository.get_primary_key())