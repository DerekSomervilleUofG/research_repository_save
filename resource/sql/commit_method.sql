CREATE TABLE IF NOT EXISTS commit_method(
    commit_method_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    lines_added INTEGER,
    lines_changed INTEGER,
    lines_removed INTEGER,
    lines_same INTEGER,
    lines_similar INTEGER,
    amendment_type TEXT,
    method_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    commit_id INTEGER NOT NULL,
    FOREIGN KEY(method_id) REFERENCES method(method_id),
    FOREIGN KEY(class_id) REFERENCES class(class_id),
    FOREIGN KEY(commit_id) REFERENCES developer_commit(commit_id)
)