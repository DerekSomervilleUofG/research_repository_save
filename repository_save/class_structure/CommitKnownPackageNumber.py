from class_structure.Structure import Structure

class CommitKnownPackageNumber(Structure):

    def __init__(self, commit_id, number_of_unknown, number_of_known, developer_id, repository_id):
        super().__init__(commit_id, commit_id)
        self.commit_id = commit_id
        self.number_of_unknown = number_of_unknown
        self.number_of_known = number_of_known
        self.developer_id = developer_id
        self.repository_id = repository_id 
        
    
    def get_commit_id(self):
        return self.commit_id
    
    def get_number_of_unknown(self):
        return self.number_of_unknown
    
    def get_number_of_known(self):
        return self.number_of_known
    
    def get_developer_id(self):
        return self.developer_id
    
    def get_repository_id(self):
        return self.repository_id