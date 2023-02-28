import sqlite3

conn = sqlite3.connect('../musicDB.db',check_same_thread=False)
cursor = conn.cursor()
cursor.execute("SELECT * FROM songs")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()