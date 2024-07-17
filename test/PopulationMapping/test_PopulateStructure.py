from repository_save.population_mapping.PopulateStructure import PopulateStructure
from unittest import TestCase

class TestPopulateStructure(TestCase):

    populate_structure = PopulateStructure()

    def test_get_insert_columns(self):
        self.assertEqual(" name", self.populate_structure.get_insert_columns())

    def test_generate_insert_values(self):
        columns = "first_column, second_column, third_column"
        self.assertEqual(" VALUES ( ?, ?, ? ) ", self.populate_structure.generate_insert_values(columns))

    def test_generate_insert_values_one_column(self):
        columns = "first_column"
        self.assertEqual(" VALUES ( ? ) ", self.populate_structure.generate_insert_values(columns))

    def test_generate_insert_with_data(self):
        table = "table_name"
        columns = "first_column"
        self.assertEqual("INSERT INTO table_name ( first_column )  VALUES ( ? ) ", self.populate_structure.generate_insert_with_data(table, columns))

    def test_geneate_insert_record(self):
        self.assertEqual("INSERT INTO table_name ( first_column )  VALUES ( ADD MAPPING )", self.populate_structure.generate_insert_record("table_name", "first_column", None))

    def test_generate_select_record(self):
        self.assertEqual("SELECT first_column FROM table_name", self.populate_structure.generate_select_record("table_name", "first_column"))

if __name__ == "__main__":
    unittest.main()