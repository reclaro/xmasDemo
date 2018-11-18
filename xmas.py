# Basic blask server to catch events
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import json




app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.sqlite3'

db = SQLAlchemy(app)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column('song_id', db.String, primary_key = False)
    title = db.Column(db.String(100))

    
db.create_all()

@app.route('/', methods = ['GET'])
def show_list(songs=None):
    songs= Song.query.all()
    return render_template("xmaslist.html", songs=songs)


@app.route('/videos', methods = ['POST'])
def playlist():
    songs_list = request.get_json()
    for s in songs_list:
        if(isNewSong(s['song_id'])):
            s = Song(song_id=s['song_id'], title=s['title'])
            db.session.add(s)
            db.session.commit()
            return ""
      
    return ""

def isNewSong(id):
    s = Song.query.filter_by(song_id=id).first()
    return s is None

if __name__ == '__main__':

    app.run(debug=True, use_reloader=True)


