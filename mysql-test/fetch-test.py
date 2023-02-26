import mysql.connector

cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='musicDB')

cursor = cnx.cursor()


cursor.execute("SELECT * FROM songs")


rows = cursor.fetchall()


for row in rows:
    print(row[1])

cursor.close()
cnx.close()


