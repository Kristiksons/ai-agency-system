from db.database import get_connection, init_db

init_db()

conn = get_connection()
cursor = conn.cursor()

posts = [
    ("How to get clients on Instagram", 120, 18, 30, "reel"),
    ("Marketing mistakes businesses make", 90, 25, 40, "carousel"),
    ("3 ways to grow your brand", 60, 10, 12, "reel"),
    ("Why your Instagram isn’t working", 200, 40, 80, "reel"),
]

i = 0

while i < len(posts):
    cursor.execute("""
    INSERT INTO posts (caption, likes, comments, saves, post_type)
    VALUES (?, ?, ?, ?, ?)
    """, posts[i])
    i += 1

conn.commit()
conn.close()

print("Seed done 🔥")
