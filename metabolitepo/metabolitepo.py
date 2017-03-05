# All IOptimizeMPrts
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort,\
     render_template, flash

app = Flask(__name__)  # Create the application instance
app.config.from_object(__name__)  # Load config from this file

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, "OptimizeMP.db"),
    SECRET_KEY="development key",
    USERNAME="admin",
    PASSWORD="default"
))
app.config.from_envvar("MPO_SETTINGS", silent=True)  # Takes precedence


def connect_db():
    """ Connects to the specific database """
    rv = sqlite3.connect(app.config["DATABASE"])
    rv.row_factory = sqlite3.Row
    return rv
