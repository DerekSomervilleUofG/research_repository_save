CREATE TABLE IF NOT EXISTS developer_experience(
    developer_experience_id INTEGER PRIMARY KEY autoincrement,
    repository_name TEXT,
    language TEXT,
	pull_date TEXT, 
    developer_id INTEGER NOT NULL,
    FOREIGN KEY(developer_id) REFERENCES developer(developer_id)
)