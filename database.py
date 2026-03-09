import sqlite3

conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
password TEXT
)
""")

# Create messages table
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
message TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")