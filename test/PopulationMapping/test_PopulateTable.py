from repository_save.population_mapping.PopulateTable import PopulateTable
from repository_save.data_source.DBExecuteSQL import DBExecuteSQL
from unittest import TestCase

class TestPopulateTable(TestCase):

    db_execute_sql = DBExecuteSQL()
    populate_table = PopulateTable(db_execute_sql)

    def test_generate_insert_values(self):
        columns = "first_column, second_column, third_column"
        self.assertEqual(" VALUES ( ?, ?, ? ) ", self.populate_table.generate_insert_values(columns))

    def test_generate_insert_values_one_column(self):
        columns = "first_column"
        self.assertEqual(" VALUES ( ? ) ", self.populate_table.generate_insert_values(columns))

    def test_generate_insert_with_data(self):
        table = "table_name"
        columns = "first_column"
        self.assertEqual("INSERT INTO table_name ( first_column )  VALUES ( ? ) ", self.populate_table.generate_insert_with_data(table, columns))

    def test_geneate_insert_record(self):
        self.assertEqual("INSERT INTO table_name ( first_column )  VALUES ( ADD MAPPING )", self.populate_table.generate_insert_record("table_name", "first_column", None))

    def test_generate_select_record(self):
        self.assertEqual("SELECT first_column FROM table_name", self.populate_table.generate_select_record("table_name", "first_column"))

if __name__ == "__main__":
    unittest.main()