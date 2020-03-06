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

#Home Page
@app.route('/')
def homepage():
    return render_template("pages/index.html")

#viewfilms page
@app.route('/viewfilms')
def viewfilms():
    movielist = films=mongo.db.films.find()
    return render_template("pages/viewfilms.html",movie=movielist)

#viewreviews page
@app.route('/viewreviews')
def viewreviews():
    reviewlist = review=mongo.db.reviews.find()
    return render_template("pages/viewreviews.html", review=reviewlist)


#addreviews page
@app.route('/addreviews', methods=['POST'])
def addreviews():
    reviews =  mongo.db.reviews.find()
    reviews.insert_one(request.find()
    return render_template("pages/addreviews.html", reviews=reviews)

#addfilm page
@app.route('/addfilms', methods=['POST'])
def addfilms():
    films =  mongo.db.films
    films.insert_one(request.find()
    return render_template("pages/addfilm.html", films=films)

#subscribe page
@app.route('/subscribe')
def subscribe():
    return render_template("pages/subscribe.html")

#login page
@app.route('/login')
def login():
    return render_template("pages/login.html")

#user home page
@app.route('/userhome')
def userhome():
    return render_template("pages/userhome.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)