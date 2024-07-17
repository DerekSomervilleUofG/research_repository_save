CREATE TABLE IF NOT EXISTS commit_class(
    commit_class_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    lines_added INTEGER,
    lines_changed INTEGER,
    lines_removed INTEGER,
    lines_same INTEGER,
    lines_similar INTEGER,
    amendment_type TEXT,
    class_id INTEGER,
    file_id INTEGER NOT NULL,
    commit_id INTEGER,
    FOREIGN KEY(class_id) REFERENCES class(class_id),
    FOREIGN KEY(file_id) REFERENCES file(file_id),
    FOREIGN KEY(commit_id) REFERENCES developer_commit(commit_id)
)