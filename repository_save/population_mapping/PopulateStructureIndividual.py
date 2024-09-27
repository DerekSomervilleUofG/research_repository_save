from repository_save.population_mapping.PopulateStructure import PopulateStructure

class PopulateStructureIndividual(PopulateStructure):

    def except_save_rows(self, sql_rows):
        last_id = 0
        for row in sql_rows:
            try:
                last_id = self.insert_with_data([row])
            except Exception:
                pass
        return last_id
    
    def save_rows(self):
        last_id = 0
        try:
            last_id = super().save_rows()
        except Exception:
            last_id = self.except_save_rows(self.sql_rows)
        return last_id