from class_structure.CodeChangeStatistic import CodeChangeStatistic
from class_structure.Structure import Structure

class StructureWithCode(Structure):

    def __init__(self, name, amendment, primary_key=0):
        super().__init__(name, primary_key)
        self.removed_by_commit = None
        self.code_change_statistic = CodeChangeStatistic(0, 0, 0)
        self.called_by = []
        self.calls_files = []
        self.calls_classes = []
        self.active = True
        self.amendment = amendment
        self.lines = []

    def __str__(self):
        self.get_name()

    def add_lines(self, new_lines):
        for line in new_lines:
            self.lines.append(line)

    def set_removed(self):
        self.set_amendment(Structure.deleted)
        self.active = False

    def set_amendment(self, amendment):
        self.amendment = amendment

    def get_content(self):
        return "\n".join(self.lines)

    def merge_code_change_statistic(self, new_code_change_satistic):
        if self.code_change_statistic == None:
            self.code_change_statistic = CodeChangeStatistic(0, 0, 0)
        self.code_change_statistic.merge(new_code_change_satistic)

    def get_called_by(self):
        return self.called_by

    def get_calls(self):
        return self.calls

    def add_called_by(self, structure):
        self.called_by.append(structure)

    def add_calls(self, structure):
        self.calls.append(structure)

    def set_removed_by_commit(self, commit=None):
        self.removed_by_commit = commit
        self.active = False

    def is_active(self):
        return self.active

    def to_string(self, spacer="\n", display_class_name=True):
        display = super().to_string(display_class_name) + " " + self.amendment
        return display