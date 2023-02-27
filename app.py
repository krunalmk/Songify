import base64
from flask import Flask , render_template, request, redirect
# import mysql.connector
import os
from dotenv import load_dotenv
import sqlite3

app = Flask(__name__) #flask app
load_dotenv() #load env
UPLOAD_FOLDER = app.root_path #os.path.join(home_dir, "upload")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

conn = sqlite3.connect('musicDB.db',check_same_thread=False)
cursor = conn.cursor()

@app.route("/song/create")
def create():
    return render_template('create.html')


@app.route("/song/createnew", methods=['POST'])
def create_new():
    title = request.form['title']
    artist = request.form['artist']
    album = request.form['album']
    mp3 = request.files["songFile"]
    print( mp3)
    songDirLoc = str(mp3.filename) #str(app.root_path+'/')+str(mp3.filename)#str(app.root_path+'/'+mp3.filename)
    # songDirLoc=songDirLoc.replace("/" , r"\/")
    print("QWERTY",songDirLoc)
    mp3.save("./static/"+ songDirLoc)
    
    # cursor.execute("INSERT INTO songs(title, artist, album, songFile) VALUES(%s, %s, %s, %s)"% (title, artist, album, songDirLoc))
    # sqlQuery = str("INSERT INTO songs(title, artist, album, songFile) VALUES(\'"+title+"\',\'"+artist+"\',\'"+album+"\',\'"+songDirLoc+ "\')")
    sqlQuery = str("INSERT INTO songs(title, artist, album, songFile) VALUES('{}', '{}', '{}', '{}')".format(title, artist, album, songDirLoc))
    print("sqlQuery", sqlQuery)
    cursor.execute(sqlQuery)
    conn.commit()

    return redirect("/")

@app.route("/song/edit/<int:id>")
def edit(id):
    sqlQuery = "SELECT * FROM songs WHERE id={}".format(id)
    print("EDIT",sqlQuery)
    cursor.execute(sqlQuery)
    row = cursor.fetchone()
    return render_template('edit.html', song=row)


@app.route("/song/delete/<int:id>")
def delete(id):
    sqlQuery = "SELECT * FROM songs WHERE id={}".format(id)
    print("EDIT",sqlQuery)
    cursor.execute(sqlQuery)
    row = cursor.fetchone()

    sqlQuery = "DELETE FROM songs WHERE id={}".format(id)
    cursor.execute(sqlQuery)
    os.remove("./static/"+row[4])

    conn.commit()
    return redirect("/")

@app.route("/song/updateSong", methods=['POST'])
def update():
    id = request.form['id']
    title = request.form['title']
    artist = request.form['artist']
    album = request.form['album']
    sqlQuery = "UPDATE songs SET title='{}', artist='{}', album='{}' WHERE id='{}'".format(title, artist, album, id)
    print("UPDATE",sqlQuery)
    cursor.execute(sqlQuery)#% 
    conn.commit()
    return redirect('/')




#home
@app.route('/')
def home():    
    rows = []
    #fetch 'songs'
    cursor.execute("SELECT * FROM songs")
    rows = cursor.fetchall()

    for eachRow in rows:
        # eachRow[4] = str(eachRow[4])
        eachRow = [eachRow[1],eachRow[2],eachRow[3],str(eachRow[4])]
        print(eachRow)
    #     # eachRow[4] = eachRow[4].encode('ascii')  # str
    #     # eachRow[4] = base64.b64decode(eachRow[4])  # bytes
    #     eachRow[4] = base64.b64decode(eachRow[4].decode('utf-8').read())  # bytes

    return render_template('index.html', rows=rows)



if __name__ == '__main__':
    app.run(debug=True)






