from unittest import TestCase
from repository_save.class_structure.Developer import Developer
from repository_save.population_mapping.PopulateDeveloper import PopulateDeveloper
from repository_save.data_source.DBExecuteSQL import DBExecuteSQL

class TestPopulateDeveloper(TestCase):
    
    developer = Developer("Derek", "derek.somerville@glasgow.ac.uk", "derek.somerville")
    populate_developer = PopulateDeveloper(DBExecuteSQL())
    
    def test_generate_row(self):
        self.assertEqual( ["'Derek'", "'derek.somerville@glasgow.ac.uk'", "'derek.somerville'"] ,self.populate_developer.generate_row(self.developer))