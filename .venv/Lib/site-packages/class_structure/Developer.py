from class_structure.Structure import Structure
class Developer(Structure):

    logging_filter = []

    def __init__(self, name, primary_key=0):
        super().__init__(name, primary_key)
        self.commits = []

    def set_developer_id(self, developer_id):
        self.set_primary_key(developer_id)

    def is_active(self):
        return True

    def add_commit(self, developer_commit):
        self.commits.append(developer_commit)

    def to_string(self, spacer="\n"):
        display = super().to_string(spacer) + spacer
        return display
