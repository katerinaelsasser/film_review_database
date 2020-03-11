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
    films=mongo.db.films.find()
    print(films)
    return render_template("pages/viewfilms.html", films=films)

#viewreviews page
@app.route('/viewreviews')
def viewreviews():
    reviews=mongo.db.reviews.find()
    print(reviews)
    return render_template("pages/viewreviews.html", reviews=reviews)


#addreviews page
@app.route('/addreviews')
def addreviews():
    return render_template("pages/addreviews.html")

#addfilm page
@app.route('/addfilms')
def addfilms():
    return render_template("pages/addfilms.html")

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
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)