from class_structure.CodeChangeStatistic import CodeChangeStatistic
from utility.ListItem import ListItem

class Structure(ListItem):

    def __init__(self, name, primary_key=0):
        super().__init__(name)
        self.active = True
        self.primary_key = primary_key
        
    def set_primary_key(self, primary_key):
        self.primary_key = primary_key
        
    def get_primary_key(self):
        return self.primary_key

    def __str__(self):
        self.get_name()

    def is_active(self):
        return self.active

    def to_string(self, spacer="\n", display_class_name=True):
        display = super().to_string(display_class_name) + " " + self.amendment
        return display