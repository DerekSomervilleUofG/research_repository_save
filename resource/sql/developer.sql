CREATE TABLE IF NOT EXISTS developer(
    developer_id INTEGER PRIMARY KEY autoincrement,
    name text NOT NULL UNIQUE
)