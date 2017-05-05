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

YES_FACE = "yes"
NO_FACE = "no"
NA_FACE = "na"

class FrameEntry(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    fID = db.Column(db.Integer, unique=True)
    jpeg_name = db.Column(db.String(80), unique=True)
    bbox0_x = db.Column(db.Integer)
    bbox0_y = db.Column(db.Integer)
    bbox0_h = db.Column(db.Integer)
    bbox0_w = db.Column(db.Integer)
    human = db.Column(db.String(40))
    confidence = db.Column(db.Numeric(0,3))
    scanner = db.Column(db.Boolean)

    def __init__(self, fID, jpeg_name, bbox0_x, bbox0_y, bbox0_w, bbox0_h, human, scanner,confidence):
        self.fID = fID
        self.jpeg_name = jpeg_name
        self.bbox0_x = bbox0_x
        self.bbox0_y = bbox0_y
        self.bbox0_h = bbox0_h
        self.bbox0_w = bbox0_w
        self.human = human
        self.confidence = confidence
        self.scanner = scanner

db.create_all()

#@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    #init_db()
    with open("static/visual_data_UI.json") as json_data:
        diction = json.load(json_data)
    arr = diction["myimages"]
    for i in arr:
        entry = FrameEntry(i["id"], i["jpeg_file"], i["bbox0"][0], i["bbox0"][1], i["bbox0"][2], i["bbox0"][3], 
            NA_FACE, i["scanner"], i["confidence"])
        if entry==None:
            print('entry is None.')
        else:
            db.session.add(entry)
    db.session.commit()
    print('Initialized the database.')
    return redirect(url_for("homepage"))

@app.route("/")
def homepage():
    # initdb_command()
    frames = FrameEntry.query.order_by(FrameEntry.fID)
    return render_template("visual_data_UI.html", frames=frames)

@app.route("/face_does_not_exist", methods=['POST'])
def face_does_not_exist():
	if (request.method == 'POST'):
		count = 0
		selectedFrames = request.get_json(force=True)['selectedFrames']
		for i in selectedFrames:
			row_changed = FrameEntry.query.filter_by(fID=i).first()
			row_changed.human = False
		db.session.commit()
		return str(row_changed.human)
	else:
		return "FAIL\n"

@app.route("/face_exists", methods=['POST'])
def face_exists():
	if (request.method == 'POST'):
		count = 0
		selectedFrames = request.get_json(force=True)['selectedFrames']
		for i in selectedFrames:
			row_changed = FrameEntry.query.filter_by(fID=i).first()
			row_changed.human=True
		db.session.commit()
		return str(row_changed.human)
	else:
		return "FAIL\n"

@app.route("/filter_frames", methods=['POST'])
def filter_frames():
    if (request.method == 'POST'):
        con_score = request.form['confidence']
        scanner_isface = request.form['scanner_isface']
        #conjunction = request.form['conjunction']
        #user_isface = request.form['human_isface']
        if con_score=="":
            return "con_score==empty string"
        elif con_score==None:
            return "con_score==None"
        else:
            return "bob"
    else:
        return "FAIL\n"


##don't edit
if __name__ == "__main__":
    app.run()