from repository_save.population_mapping.PopulateTable import PopulateTable

class PopulateCommit(PopulateTable):

    def generate_row(self, structure):
        row = []
        row.append(structure.get_name())
        code_change_statistic = structure.code_change_statistic
        row.append(code_change_statistic.lines_added)
        row.append(code_change_statistic.lines_changed)
        row.append(code_change_statistic.lines_removed)
        row.append(code_change_statistic.lines_same)
        row.append(code_change_statistic.lines_similar)
        row.append(structure.amendment)
        return row