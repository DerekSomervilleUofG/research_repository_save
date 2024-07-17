from utility.ListUtility import ListUtility
from class_structure.DeclaredStructure import DeclaredStructure

class ClassStructure(DeclaredStructure):

    def __init__(self, name, amendment, owned_by_file=None, primary_key=0):
        super().__init__(name, amendment, primary_key)
        self.owned_by_file = owned_by_file
        self.methods = []
        self.is_an_interface = False

    def add_method(self, method):
        #self.log_message("add_method", method.get_name())
        ListUtility.add_to_unique_list(self.methods, method)

    def set_owned_by_file(self, owned_by_file):
        self.owned_by_file = owned_by_file

    def to_string(self, spacer="\n", display_class_name=True):
        display = super().to_string(spacer, display_class_name)
        display += ListUtility.format_list(self.methods, display, "; ")
        return display + spacer

    def remove_from_line_when_contains(self, lines, pattern):
        for line in lines:
            if pattern in line:
                lines.remove(line)

    def get_content(self):
        test_full_declare = "    @org.junit.jupiter.api.Test"
        test_declare = "    @Test"
        test_tab_declare = "\t@Test"
        content = super().get_content()
        for method in self.methods:
            if "Test" in self.get_name():
                if test_full_declare in method.lines:
                    method.lines.remove(test_full_declare)
                if test_declare in method.lines:
                    method.lines.remove(test_declare)
                if test_tab_declare in method.lines:
                    method.lines.remove(test_tab_declare)
                self.remove_from_line_when_contains(method.lines, "@Test")
                content += "\n" + test_full_declare + "\n"
            content += method.get_content() + "\n"
        return content
    
    def __str__(self):
        return self.name + " methods:- " #+ reduce(concat, map(method: method.name, self.methods))