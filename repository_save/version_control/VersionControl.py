from abc import ABC, abstractmethod

class VersionControl(ABC):

    valid_file_types = ["java", "py", "cs", "cp", "json", "xml", "form", "sql", "yml", "md"]

    def get_content(self, raw_content):
        content = ""
        try:
            content = raw_content.data_stream.read().decode('utf-8')
        except (Exception, UnicodeDecodeError, AttributeError):
            content = ""
        return content

    def valid_file_type(self, path):
        valid = False
        if "." in path:
            split_file = path.split(".")
            if len(split_file) == 2 and split_file[-1] in self.valid_file_types:
                valid = True
        return valid

    def valid_path(self, path):
        valid = False
        if path is not None and self.valid_file_type(path) and ("/" not in path or ("src/" in path or "test/" in path or "resource" in path)):
            valid = True
        return valid
