import os
import sqlite3
from flask import Flask, url_for, request, session, g, redirect, abort, \
    render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
import json
from pprint import pprint

app = Flask(__name__)
#app.config.from_object(__name__)  load config from this file , server.py
##the sqlalchemy
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:////tmp/webdevblog.db"
app.debug = True

db = SQLAlchemy(app)

class FrameEntry(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    fID = db.Column(db.Integer, unique=True)
    jpeg_name = db.Column(db.String(80), unique=True)
    bbox0_x = db.Column(db.Integer)
    bbox0_y = db.Column(db.Integer)
    bbox0_h = db.Column(db.Integer)
    bbox0_w = db.Column(db.Integer)
    bbox1_x = db.Column(db.Integer)
    bbox1_y = db.Column(db.Integer)
    bbox1_h = db.Column(db.Integer)
    bbox1_w = db.Column(db.Integer)
    human = db.Column(db.String(40))

    def __init__(self, fID, jpeg_name, bbox0_x, bbox0_y, bbox0_w, bbox0_h, 
        bbox1_x, bbox1_y, bbox1_h, bbox1_w, human):
        self.fID = fID
        self.jpeg_name = jpeg_name
        self.bbox0_x = bbox0_x
        self.bbox0_y = bbox0_y
        self.bbox0_h = bbox0_h
        self.bbox0_w = bbox0_w
        self.bbox1_x = bbox1_x
        self.bbox1_y = bbox1_y
        self.bbox1_h = bbox1_h
        self.bbox1_w = bbox1_w
        self.human = human
        #don't we have to assign ID as well?

    def __repr__(self):
        return "POST %s by %s on %s" %(self.jpeg_name, self.author, self.date)

db.create_all()

def createPost(fID, bbox0_x, bbox0_y, bbox0_w, bbox0_h, 
    bbox1_x, bbox1_y, bbox1_w, bbox1_h, jpeg_name, human):
  '''
  Creates a BlogEntry if given valid parameters, else return None.
  '''
  # first verify components
  if len(human) <= 40 and len(jpeg_name)<=80:
      return FrameEntry(fID, jpeg_name, bbox0_x, bbox0_y, bbox0_w, bbox0_h,
        bbox1_x, bbox1_y, bbox1_h, bbox1_w, human)
  return None


# Load default config and override config from an environment variable
'''
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
'''
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

#@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    #init_db()
    with open("static/visual_data_UI.json") as json_data:
        diction = json.load(json_data)
    arr = diction["myimages"]
    for i in arr:
        post = createPost(i["id"], i["x"], i["y"], i["width"], i["height"], 
            0, 0, 0, 0, i["jpeg_file"], "n/a")
        if post==None:
            print('post is None.')
        else:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for("homepage"))
    print('Initialized the database.')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def populate_db(file):
	f = json.load(open(file))
	for el in f["myimages"]:
		post = createPost(el["id"], el["x"], el["y"], el["width"], el["height"], 
			0, 0, 0, 0, el["jpeg_file"], el["human"])
		if (FrameEntry.query.filter_by(fID=el["id"]).first()==None):
			db.session.add(post)
			count+=1
	return str(count)

@app.route("/")
def homepage():
    return render_template("visual_data_UI.html")

@app.route("/wrong_bbox", methods=['POST'])
def wrong_bbox():
	print("running wrong_bbox...")
	if (request.method == 'POST'):
		count = 0
		selectedFrames = request.get_json(force=True)['selectedFrames']
		for i in selectedFrames:
			row_changed = FrameEntry.query.filter_by(fID=i).first()
			row_changed.human="incorrect"
		db.session.commit()
		return str(row_changed.human)
	else:
		return "FAIL\n"

@app.route("/correct_bbox", methods=['POST'])
def correct_bbox():
	print("running correct_bbox...")
	if (request.method == 'POST'):
		count = 0
		selectedFrames = request.get_json(force=True)['selectedFrames']
		for i in selectedFrames:
			row_changed = FrameEntry.query.filter_by(fID=i).first()
			row_changed.human="correct"
		db.session.commit()
		return str(row_changed.human)
	else:
		return "FAIL\n"

##don't edit
if __name__ == "__main__":
    app.run()