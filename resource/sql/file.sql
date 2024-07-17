CREATE TABLE IF NOT EXISTS file(
    file_id INTEGER PRIMARY KEY autoincrement,
    name TEXT,
    is_active INTEGER DEFAULT 1,
    latest TEXT,
    syntax_error INTEGER,
    package_id INTEGER,
    repository_id INTEGER,
    FOREIGN KEY(package_id) REFERENCES package(package_id),
    FOREIGN KEY(repository_id) REFERENCES repository(repository_id)
)