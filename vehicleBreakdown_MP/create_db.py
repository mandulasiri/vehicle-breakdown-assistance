import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    password TEXT
)
""")

# Requests table
cursor.execute("""
CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vehicle TEXT,
    problem TEXT,
    location TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Database tables created successfully!")