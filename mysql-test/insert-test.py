import mysql.connector

cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='musicDB')

cursor = cnx.cursor()

#input data to insert into database


title = "Song 6"

#shortnotes = input("ShortNotes: ")
#price = 2347.00

short_notes = "This is a sample product"
price = 19.99




#add_product = cursor.execute("INSERT INTO songs(title, short_notes, price) VALUES('{title}', '{short_notes}', '{price}')")


add_product = ("INSERT INTO songs (title, artist, album, songFile) VALUES (%s, %s, %s, %s)")
data_product = (title, short_notes, price)
cursor.execute(add_product, data_product)
#cursor.execute(add_product)
cnx.commit()

print("\n\n Data uploaded to database successfully!!\n")

cursor.close()
cnx.close()
