import sqlite3
from pathlib import Path

DB_NAME = Path(__file__).with_name("students.db")

def get_connection():
    """Return a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    """Create the students table if it does not already exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL,
                marks REAL NOT NULL DEFAULT 0
            )
        """)
        conn.commit()
