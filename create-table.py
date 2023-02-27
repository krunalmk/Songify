import sqlite3
 
conn = sqlite3.connect('musicDB.db')
cursor = conn.cursor()
# Creating table as per requirement
sql = "CREATE TABLE songs(id int auto_increment primary key not null,title text not null,artist text not null,album text not null,songFile longblob not null )"
cursor.execute(sql)
for i in range (10):
    sql = "INSERT INTO songs (id,title,artist,album,songFile) values ("+str(i)+",\'Hi\',\'HiHi\',\'HiHiHi\',\'HAAAAHHHi\')"
    cursor.execute(sql)
    
conn.commit()
print("Table created successfully.....")