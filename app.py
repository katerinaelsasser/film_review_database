# import section
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

#mongodb
app = Flask(__name__)
app.config['MONGO_URI'] = os.environ["MONGO_URI"]
app.config['MONGO_DBNAME'] = os.environ['MONGO_DBNAME']
mongo = PyMongo(app)

#linking the index
@app.route('/')
@app.route('/get_films')
def get_films():
    return render_template("index.html", film.mongo.db.film.find())

@app.route("/add_review")
def add_review():
    return render_template("add_review.html") 

@app.route('/update_film/<film_id>', methods=["POST"])
def update_film(film_id):
    film = mongo.db.film
    film.update( {'_id': ObjectId(film_id)},
    {
        'film_name':request.form.get('film_name'),
        'film_year':request.form.get('film_year'),
        'film_director': request.form.get('film_director'),
        'film_genre': request.form.get('film_genre'),
        'film_rating': request.form.get('film_rating'),
        'film_length': request.form.get('film_length'),
        'film_description': request.form.get('film_description'),
    })
    return redirect(url_for('get_films'))       
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)