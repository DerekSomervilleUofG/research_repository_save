from repository_save.version_control.VersionControl import VersionControl
from utility.ReadWriteFile import ReadWriteFile

import os, time
from git import Repo

class VersionControlGit(VersionControl):
    
    read_write_file = ReadWriteFile()

    def get_author_date(self, date):
        gm_time = time.gmtime(date)
        date = str(gm_time.tm_year) + "-" + str(gm_time.tm_mon) + "-" + str(gm_time.tm_mday) + " " + str(gm_time.tm_hour) + ":" + str(gm_time.tm_min) + ":" + str(gm_time.tm_sec)
        return date

    def get_repo(self, repo_name, repo_path):
        self.read_write_file.fix_working_directory()
        work_directory = os.getcwd()
        if "http" in repo_path:
            if not os.path.isdir(repo_name):
                os.mkdir(repo_name)
            if not os.path.isdir(repo_name):
                Repo.clone_from(repo_path, repo_name)
        repo = Repo(repo_name)
        os.chdir(work_directory)
        return repo

    def get_commits_on_branch(self, git_repository: Repo, branch_names=None, limit=None):
        _branch_names = ['master', 'trunk', 'develop', 'main', 'dev'] if branch_names is None else branch_names

        result = list()

        for branch_name in _branch_names:
            if branch_name in git_repository.heads:
                current = git_repository.heads[branch_name].commit
                result.insert(0, current)

                while len(current.parents) > 0 and (limit is None or len(result) < limit):
                    result.insert(0, current.parents[0])
                    current = current.parents[0]

                return result

        return None

    

if __name__ == "__main__":
    version_control_git = VersionControlGit()
    repo = version_control_git.get_repo("output/dummy-repo","https://github.com/DerekSomervilleUofG/dummy-repo/.git")
    print("Number of commits", len(version_control_git.get_commits_on_branch(repo, None, None)))
