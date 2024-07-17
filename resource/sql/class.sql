CREATE TABLE IF NOT EXISTS class(
    class_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    is_active INTEGER DEFAULT 1,
    file_id INTEGER NOT NULL,
    FOREIGN KEY(file_id) REFERENCES file(file_id)
)