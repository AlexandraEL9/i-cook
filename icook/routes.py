from flask import render_template
from icook import app, db
from icook.models import Category, Recipe


@app.route("/")
def home():
    return render_template("base.html")