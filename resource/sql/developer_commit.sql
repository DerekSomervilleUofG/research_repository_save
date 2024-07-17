CREATE TABLE IF NOT EXISTS developer_commit(
    commit_id TEXT PRIMARY KEY,
    author TEXT NOT NUll,
    authored_date TEXT NOT NULL,
    number_of_repo_packages INTEGER,
    number_of_repo_files INTEGER,
    number_of_repo_classes INTEGER,
    number_of_repo_methods INTEGER,
    message TEXT,
    repository_id INTEGER NOT NULL,
    developer_id INTEGER NOT NULL,
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id),
    FOREIGN KEY(developer_id) REFERENCES developer(developer_id)
   )
