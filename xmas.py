# Basic blask server to catch events
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.sqlite3'

db = SQLAlchemy(app)

# default YQHsXMglC9A
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column('song_id', db.String, primary_key = False)
    title = db.Column(db.String(100))

    #def __init__(self, *args, **kwargs):
    
db.create_all()

@app.route('/', methods = ['GET'])
def show_list(songs=None):
    songs= Song.query.all()
    return render_template("xmaslist.html", songs=songs)


@app.route('/videos/<video>', methods = ['POST'])
def user(video):
      s = Song(song_id=video.split('@')[0], title=video.split('@')[1])
      db.session.add(s)
      db.session.commit()
      return ""
      
if __name__ == '__main__':

    app.run(debug=True, use_reloader=True)


