import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

DBNAME = os.environ.get("DB_NAME")
PWD = os.environ.get("DB_PWD")
USERNAME = os.environ.get("DB_USERNAME")
HOST = os.environ.get("DB_HOST")

cnx = mysql.connector.connect(user=USERNAME, password=PWD, host=HOST, database=DBNAME)
cursor = cnx.cursor()

id = 2
cursor.execute("SELECT * FROM songs WHERE id=%s", (id,))
row = cursor.fetchone()

print(row[1])
