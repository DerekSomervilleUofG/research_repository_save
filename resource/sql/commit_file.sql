CREATE TABLE IF NOT EXISTS commit_file(
    commit_file_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    lines_added INTEGER,
    lines_changed INTEGER,
    lines_removed INTEGER,
    lines_same INTEGER,
    lines_similar INTEGER,
    amendment_type TEXT,
    file_id INTEGER NOT NULL,
    commit_id INTEGER NOT NULL,
    package_id INTEGER NOT NULL,
    repository_id INTEGER NOT NULL,
    FOREIGN KEY(file_id) REFERENCES file(file_id),
    FOREIGN KEY(commit_id) REFERENCES developer_commit(commit_id),
    FOREIGN KEY(package_id) REFERENCES package(package_id),
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id)
)