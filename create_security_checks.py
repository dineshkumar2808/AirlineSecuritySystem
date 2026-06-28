from utils.db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS security_checks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    passenger_id INTEGER,
    flight_id INTEGER,
    baggage_scan TEXT,
    metal_detector TEXT,
    risk_level TEXT,
    security_status TEXT,
    officer_name TEXT,
    remarks TEXT,
    check_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(passenger_id) REFERENCES passengers(id),
    FOREIGN KEY(flight_id) REFERENCES flights(id)
)
""")

conn.commit()
conn.close()

print("Security Checks Table Created")