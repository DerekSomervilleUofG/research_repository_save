CREATE TABLE IF NOT EXISTS repository(
    repository_id INTEGER PRIMARY KEY,
    url TEXT NOT NULL UNIQUE,
    name TEXT
)