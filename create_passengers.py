from utils.db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS passengers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    passport_no TEXT UNIQUE NOT NULL,
    nationality TEXT,
    gender TEXT,
    phone TEXT,
    email TEXT
)
""")

conn.commit()
conn.close()

print("Passengers table created")