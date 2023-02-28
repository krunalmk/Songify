import sqlite3

conn = sqlite3.connect('../musicDB.db',check_same_thread=False)
cursor = conn.cursor()

title = "Song 6"
artist = "Sample artist"
album = "Sample Album"


sqlQuery = "INSERT INTO songs (title, artist, album, songFile) VALUES ('{}', '{}', '{}', '{}')".format(title, artist, album, "/someLocation")
cursor.execute( sqlQuery)
conn.commit()

print("\n\n Data uploaded to database successfully!!\n")

cursor.close()
conn.close()
