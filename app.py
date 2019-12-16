import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'film_database'
app.config["MONGO_URI"] = 'mongodb+srv://kit_22:MiloCat0104@filmreviews-dqtff.mongodb.net/film_database?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_films')
def get_films():
    return render_template("films.html", films=mongo.db.films.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)