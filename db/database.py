import sqlite3

def get_connection():
    return sqlite3.connect("data/ig.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        caption TEXT,
        likes INTEGER,
        comments INTEGER,
        saves INTEGER,
        post_type TEXT
    )
    """)

    conn.commit()
    conn.close()
