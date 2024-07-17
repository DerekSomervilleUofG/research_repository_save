CREATE TABLE IF NOT EXISTS file_method(
    file_method_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    lines_added INTEGER,
    lines_changed INTEGER,
    lines_removed INTEGER,
    lines_same INTEGER,
    lines_similar INTEGER,
    file_id INTEGER NOT NULL,
    commit_id INTEGER,
    prior_knowledge_id INTEGER,
    FOREIGN KEY(file_id) REFERENCES file(file_id),
    FOREIGN KEY(commit_id) REFERENCES developer_commit(commit_id),
    FOREIGN KEY(prior_knowledge_id) REFERENCES prior_knowledge(prior_knowledge_id)

)