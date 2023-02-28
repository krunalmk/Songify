import sqlite3
 
conn = sqlite3.connect('musicDB.db')
cursor = conn.cursor()

# Creating table as per requirement
sql = "CREATE TABLE songs(id integer primary key AUTOINCREMENT,title text not null,artist text not null,album text not null,songFile text not null )"
cursor.execute(sql)
conn.commit()
conn.close()
print("Table created successfully.....")