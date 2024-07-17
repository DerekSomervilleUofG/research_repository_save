from class_structure.Structure import Structure
from unittest import TestCase

class TestStructure(TestCase):

    structure = Structure("name")

    def test_get_name(self):
        self.assertEqual("name", self.structure.get_name())

    def test_default_primary_key(self):
        self.assertEqual(0, self.structure.get_primary_key())

    def test_set_primary_key(self):
        self.structure.set_primary_key(1)
        self.assertEqual(1, self.structure.get_primary_key())