import base64
from flask import Flask , render_template, request, redirect
import mysql.connector
import os
from dotenv import load_dotenv

app = Flask(__name__) #flask app
load_dotenv() #load env



DBNAME = os.environ.get("DB_NAME")
PWD = os.environ.get("DB_PWD")
USERNAME = os.environ.get("DB_USERNAME")
HOST = os.environ.get("DB_HOST")

cnx = mysql.connector.connect(user=USERNAME, password=PWD, host=HOST, database=DBNAME)
cursor = cnx.cursor()



@app.route("/song/create")
def create():
    return render_template('create.html')


@app.route("/song/createnew", methods=['POST'])
def create_new():
    title = request.form['title']
    short_notes = request.form['shortnotes']
    price = request.form['price']
    cursor.execute("INSERT INTO songs(title,short_notes,price) VALUES(%s, %s, %s)", (title, short_notes, price))

    mp3 = request.files["audioFileChooser"]
    print( mp3)
    print(type(mp3)) #This is type string
    # ans = base64.b64decode(bytes(mp3, 'utf-8'))
    rv = base64.b64encode(mp3.read())  # bytes
    rv = rv.decode('ascii')  # str
    # return rv
    print("HI dear", rv)
    # print(type(ans)) #This is type bytes
    # with open("audioToSave.webm", "wb") as fh:
    #     fh.write(ans)
    # theAnswer = 'no'
    # return theAnswer
    return redirect("/")

@app.route("/song/edit/<int:id>")
def edit(id):
    #select based on id
    #cursor.execute("SELECT * FROM songs WHERE id=?",(id,))
    cursor.execute("SELECT * FROM songs WHERE id=%s", (id,))
    row = cursor.fetchone()
    return render_template('edit.html', song=row)


@app.route("/song/delete/<int:id>")
def delete(id):
    cursor.execute("DELETE FROM songs WHERE id=%s", (id,))
    return redirect("/")

#update
@app.route("/song/updateSong", methods=['POST'])
def update():
    id = request.form['id']
    title = request.form['title']
    short_notes = request.form['shortnotes']
    price = request.form['price']
    cursor.execute("UPDATE songs SET title=%s, short_notes=%s, price=%s WHERE id=%s", (title, short_notes, price, id))
    return redirect('/')




#home
@app.route('/')
def home():    
    #fetch 'songs'
    cursor.execute("SELECT * FROM songs")
    rows = cursor.fetchall()

    return render_template('index.html', rows=rows)



if __name__ == '__main__':
    app.run(debug=True)






