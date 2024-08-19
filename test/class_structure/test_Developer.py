from unittest import TestCase
from repository_save.class_structure.Developer import Developer


class TestDeveloper(TestCase):
    
    developer = Developer("Derek", "derek.somerville@glasgow.ac.uk", "derek.somerville")
    
    def test_get_name(self):
        self.assertEqual("Derek", self.developer.get_name())