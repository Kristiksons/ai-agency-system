import sqlite3
import json
import os

DB_PATH = "data.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client TEXT,
        niche TEXT,
        data TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_history(client_name, niche, data):

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        INSERT INTO history (client, niche, data)
        VALUES (?, ?, ?)
    """, (client_name, niche, json.dumps(data)))

    conn.commit()
    conn.close()


def load_history():

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT client, niche, data FROM history ORDER BY id DESC")
    rows = c.fetchall()

    conn.close()

    result = []

    i = 0
    while i < len(rows):
        result.append({
            "client": rows[i][0],
            "niche": rows[i][1],
            "data": json.loads(rows[i][2])
        })
        i += 1

    return result