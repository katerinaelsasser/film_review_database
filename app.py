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
@app.route('/', methods=['GET', 'POST'])
@app.route('/homepage', methods=['GET', 'POST'])
def home_page():
    return render_template("index.html") 

#Film Database
@app.route('/viewfilms')
def viewfilms():
    return render_template("viewfilms.html")

@app.route("/viewreviews")
def viewreviews():
    return render_template("viewreviews.html") 

@app.route("/addreviews")
def addreviews():
    return render_template("addreview.html") 
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)