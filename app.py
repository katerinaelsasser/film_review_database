# import section
import os
from flask import Flask, render_template, redirect, url_for, request
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
@app.route('/view/movies')
def viewmovies():
    return render_template("pages/viewfilms.html")

#individual film page
@app.route('/view/movies/{{movie.imdbID}}', methods=['GET','POST'])
def movieID():
    reviews =  mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return render_template("pages/individualfilm.html")

#login page   
@app.route('/login')
def login():
    return render_template("pages/login.html")
    
#user home page
@app.route('/userhome')
def userhome():
    return render_template("pages/userhome.html")

#Delete reviews
@app.route('/deletereviews', methods=['GET','POST'])
def deletereviews():
    reviews=mongo.db.reviews.find()
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    print(reviews)
    return render_template("pages/viewallreviews.html", reviews=reviews)

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)