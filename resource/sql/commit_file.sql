CREATE TABLE IF NOT EXISTS commit_file(
    commit_file_id INTEGER PRIMARY KEY autoincrement,
    amendment_type TEXT,
    file_id INTEGER NOT NULL,
    commit_id INTEGER NOT NULL,
    FOREIGN KEY(file_id) REFERENCES file(file_id),
    FOREIGN KEY(commit_id) REFERENCES developer_commit(commit_id)
)