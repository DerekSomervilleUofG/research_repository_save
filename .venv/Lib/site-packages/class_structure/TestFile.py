from class_structure.ClassStructure import ClassStructure
from class_structure.Structure import Structure

class TestFile(Structure):

    def __init__(self, name, class_used, primary_key=0):
        super().__init__(name, Structure.added, primary_key)
        self.class_used = class_used
        self.new_class = ClassStructure(class_used.get_name(), Structure.added)

    def get_content(self):
        content = super().get_content()
        content += "\n" + self.new_class.get_content()
        content += "\n}"
        return content

