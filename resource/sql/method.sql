CREATE TABLE IF NOT EXISTS method(
    method_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    is_active INTEGER DEFAULT 1,
    class_id INTEGER NOT NULL,
    FOREIGN KEY(class_id) REFERENCES class(class_id)
)