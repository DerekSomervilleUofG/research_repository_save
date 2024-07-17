CREATE TABLE IF NOT EXISTS package(
    package_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    is_active INTEGER,
    repository_id INTEGER,
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id)

)