""" Main Flask File"""
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort,\
     render_template, flash

app = Flask(__name__)  # Create the application instance
app.config.from_object(__name__)  # Load config from this file
# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, "metabolitepo.db"),  # local db
    SECRET_KEY="development key",
    USERNAME="admin",
    PASSWORD="default"
))
app.config.from_envvar("MPO_SETTINGS", silent=True)  # Takes precedence


@app.route("/")
def homepage():
    return render_template("home.html")


@app.route("/search", methods=["POST"])
def search():
    if not valid_search:
        abort(401)

    cell = request.form["cell"]
    cell_strain = request.form["cell_strain"]
    input_chemical = request.form["input_chemical"]
    output_chemical = request.form["output_chemical"]
    abort(401)
    
    # ...Matching process 

if __name__ == "__main__":
    app.run()


def connect_db():
    """ Connects to database """
    rv = sqlite3.connect(app.config["DATABASE"])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """ Opens a database connection if there is none yet for the
    current application context """
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """ Close the db again at the end of the request """
    if hasattr(g, "sqlite_db"):
        g.sqlite_db.close()


def init_db():
    db = get_db()
    with app.open_resource("schema.sql", mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command("initdb")
def initdb_command():
    """ Initializes the database """
    init_db()
    print("Database Initialized")
