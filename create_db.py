from utils.db import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
""")

cursor.execute("""
INSERT INTO users(username,password,role)
VALUES('admin','admin123','Admin')
""")

conn.commit()
conn.close()

print("Database Created")