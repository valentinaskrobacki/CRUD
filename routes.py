from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Movie

@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

