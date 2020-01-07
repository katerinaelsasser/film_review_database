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
@app.route('/display_films')
def display_films():
    return render_template("index.html")

@app.route('/add_reviews')
def add_reviews():
    return render_template('review.html',
                           categories=mongo.db.reviews.find())


@app.route('/insert_review', methods=['POST'])
def insert_task():
    reviews =  mongo.db.reviews
    reviewss.insert_one(request.form.to_dict())
    return redirect(url_for('display_films'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)