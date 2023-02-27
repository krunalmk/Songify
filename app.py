import base64
from flask import Flask , render_template, request, redirect
import mysql.connector
import os
from dotenv import load_dotenv

app = Flask(__name__) #flask app
load_dotenv() #load env
UPLOAD_FOLDER = app.root_path #os.path.join(home_dir, "upload")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



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
    artist = request.form['artist']
    album = request.form['album']
    mp3 = request.files["songFile"]
    print( mp3)
    # ans = base64.b64decode(bytes(mp3, 'utf-8'))
    mp3.save(app.config['UPLOAD_FOLDER'])
    
    
    
    # songBLOB = base64.b64encode(mp3.read()) #.decode('ascii')  # bytes
    # # print("songBLOB", songBLOB)
    # file_name = mp3.filename
    # print("QWERTY", file_name)
    # with open("QWERTY", "wb") as file:  	# open in binary mode 
    #     file.write(mp3)


    # songBLOB = songBLOB.decode('ascii')  # str
    # cursor.execute("INSERT INTO songs(title, artist, album, songFile) VALUES(%s, %s, %s, %s)", (title, artist, album, songBLOB))

    # return rv
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
    artist = request.form['artist']
    album = request.form['album']
    cursor.execute("UPDATE songs SET title=%s, short_notes=%s, price=%s WHERE id=%s", (title, artist, album, id))
    return redirect('/')




#home
@app.route('/')
def home():    
    rows = []
    #fetch 'songs'
    cursor.execute("SELECT * FROM songs")
    rows = cursor.fetchall()

    # for eachRow in rows:
    #     # eachRow[4] = eachRow[4].encode('ascii')  # str
    #     # eachRow[4] = base64.b64decode(eachRow[4])  # bytes
    #     eachRow[4] = base64.b64decode(eachRow[4].decode('utf-8').read())  # bytes

    return render_template('index.html', rows=rows)



if __name__ == '__main__':
    app.run(debug=True)






