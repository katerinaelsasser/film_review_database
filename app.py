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
@app.route('/homepage')
def homepage():
    return render_template("pages/index.html")

#viewfilms page
@app.route('/viewfilms')
def viewfilms():
    return render_template("pages/viewfilms.html")

#viewreviews page
@app.route('/viewreviews')
def viewreviews():
    return render_template("pages/viewreviews.html")

#addreviews page
@app.route('/addreviews')
def addreviews():
    return render_template("pages/addreviews.html")

#addreviews page
@app.route('/addfilms')
def addfilms():
    return render_template("pages/addfilm.html")

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