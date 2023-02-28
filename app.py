from flask import Flask , render_template, request, redirect
import os
import sqlite3

app = Flask(__name__) #flask app
UPLOAD_FOLDER = app.root_path
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

conn = sqlite3.connect('musicDB.db',check_same_thread=False)
cursor = conn.cursor()

@app.route("/song/create")
def create():
    return render_template('create.html')


@app.route("/song/search", methods=["POST"])
def search():
    songs = []
    attribute = request.form['attribute']
    attributeValue = request.form['attributeValue']
    sqlQuery = "SELECT * FROM songs WHERE {}='{}'".format(attribute,attributeValue)
    if cursor.execute(sqlQuery):
        songs = cursor.fetchall()
    return render_template('index.html', songs=songs)


@app.route("/song/createnew", methods=['POST'])
def create_new():
    title = request.form['title']
    artist = request.form['artist']
    album = request.form['album']
    mp3 = request.files["songFile"]
    songDirLoc = str(mp3.filename)
    mp3.save("./static/"+ songDirLoc)
    sqlQuery = str("INSERT INTO songs(title, artist, album, songFile) VALUES('{}', '{}', '{}', '{}')".format(title, artist, album, songDirLoc))
    cursor.execute(sqlQuery)
    conn.commit()
    return redirect("/")

@app.route("/song/edit", methods = ['POST'])
def edit():
    id = request.form['attributeValue']
    sqlQuery = "SELECT * FROM songs WHERE id={}".format(id)
    cursor.execute(sqlQuery)
    row = cursor.fetchone()
    return render_template('edit.html', song=row)


@app.route("/song/view", methods = ['POST'])
def view():
    id = request.form['attributeValue']
    sqlQuery = "SELECT * FROM songs WHERE id={}".format(id)
    cursor.execute(sqlQuery)
    row = cursor.fetchone()
    return render_template('view.html', song=row)


@app.route("/song/delete", methods = ['POST'])
def delete():
    id = request.form['attributeValue']
    sqlQuery = "SELECT songFile FROM songs WHERE id={}".format(id)
    cursor.execute(sqlQuery)
    row = cursor.fetchone()

    sqlQuery = "DELETE FROM songs WHERE id={}".format(id)
    cursor.execute(sqlQuery)
    os.remove("./static/"+row[0])

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
    cursor.execute(sqlQuery)
    conn.commit()
    return redirect('/')

#home
@app.route('/')
def home():    
    rows = []
    cursor.execute("SELECT * FROM songs")
    songs = cursor.fetchall()
    return render_template('index.html', songs=songs)
    

if __name__ == '__main__':
    app.run(debug=True)






