import sqlite3
import os

DB_PATH = os.path.join("backend", "applications.db")

def initialize_database():
    print(f"📦 Initializing local database asset at: {DB_PATH}")
    
    # Establish local file connection
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create structural tracking schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            status TEXT DEFAULT 'Applied',
            date_tracked TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database structural schema verified and locked.")

if __name__ == "__main__":
    initialize_database()