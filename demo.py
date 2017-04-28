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

db.create_all()

# Load default config and override config from an environment variable
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

@app.route("/")
def homepage():
    return render_template("demo.html")

@app.route("/updateFrames", methods=['POST'])
def updateFrames():
    print("C'S GET DEGREES")
    print(request)
    return "KMS"#render_template("visual_data_UI.html")
	#selectedFrames = request.form["selectedImages"]
	#print(selectedFrames)
	#ta = get_db()

	#data.update().values(human='yes').where(
    #    users.fID==select([selectedFrames]).\
    #                as_scalar()
    #    )

    #sqlalchemy command...
	#sqlalchemy.sql.expression.update(data)
	#selected_frames = request.form["id"]

##don't edit
if __name__ == "__main__":
    app.run()
