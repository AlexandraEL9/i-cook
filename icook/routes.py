from flask import render_template
from icook import app, db
from icook.models import Category, Recipe


@app.route("/")
def home():
    return render_template("recipes.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")