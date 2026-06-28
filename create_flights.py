from utils.db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS flights(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_no TEXT NOT NULL UNIQUE,
    airline_name TEXT NOT NULL,
    source TEXT NOT NULL,
    destination TEXT NOT NULL,
    departure_time TEXT NOT NULL,
    arrival_time TEXT NOT NULL,
    status TEXT DEFAULT 'Scheduled'
)
""")

conn.commit()
conn.close()

print("Flights table created successfully")