from repository_save.population_mapping.PopulateTable import PopulateTable
from utility.ListUtility import ListUtility

class PopulateStructure(PopulateTable):

    def __init__(self):
        super().__init__()
        self.table_name = "structure"
        self.all_columns = "primary_key, name"
        self.primary_key = "primary_key"
        self.primary_key_col = 0
        self.name_col = 1
        self.foreign_key_col = 2

    def update_structure_id(self, structures, sql_structures):
        structure_dict = {}
        for sql_structure in sql_structures:
            structure = ListUtility.find_in_list_by_name(structures, sql_structure[self.name_col])
            if structure is not None:
                structure.set_primary_key(sql_structure[self.primary_key_col])
                structure_dict[sql_structure[self.primary_key_col]] = structure
        return structure_dict

    def populate_structure_id(self, structures, structure_id, structure_dict):
        if structures is not None:
            for structure in reversed(structures):
                if structure.is_active():
                    structure.set_primary_key(structure_id)
                    structure_dict[structure_id] = structure
                    structure_id -= 1


    def get_structures(self, structures, foreign_key):
        sql_structures = self.select_record_by_foreign_key(foreign_key)
        structure_dict = self.update_structure_id(structures, sql_structures)
        unsaved_structures = self.get_unsaved_structures(structures, foreign_key, structure_dict)
        return unsaved_structures, structure_dict

    def get_unsaved_structures(self, structures, foreign_key, structure_dict):
        unsaved_structures = []
        for structure in structures:
            if structure.package_id == 0:
                structure_id = self.add_row(self.generate_row(structure, foreign_key))
                unsaved_structures.append(structure)
                if structure_id > 0:
                    self.populate_structure_id(unsaved_structures, structure_id, structure_dict)
                    unsaved_structures = []
        return unsaved_structures

    def save_rows(self):
        structure_id = super().save_rows()
        structure_dict = {}
        if len(self.list_structures) > 0:
            self.populate_structure_id(self.list_structures, structure_id, structure_dict)
            self.list_structures = []
