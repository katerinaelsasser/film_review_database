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
    return render_template("pages/index.html", TitlePage="Home")

#viewfilms page
@app.route('/view/movies', methods=['GET'])
def viewmovies():
    movies = mongo.db.movies.find()
    reviews = mongo.db.reviews.find()
    print(movies, reviews)
    return render_template("pages/viewfilms.html", movies=movies, reviews=reviews, TitlePage="Find A Movie")

#leave review page
@app.route('/add/review', methods=['POST'])
def addreview():
    reviews =  mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return render_template("pages/addreview.html", reviews=reviews, TitlePage="Leave A Review")

#login page   
@app.route('/login')
def login():
    return render_template("pages/login.html", TitlePage="Login")
    
#user home page
@app.route('/userhome')
def userhome():
    return render_template("pages/userhome.html", TitlePage="Admin")

#View All Reviews
@app.route('/viewreviews', methods=['GET','POST'])
def viewreviews():
    reviews=mongo.db.reviews.find()
    print(reviews)
    return render_template("pages/viewallreviews.html", reviews=reviews)

#Delete reviews
#@app.route('/deletereviews/<review_id>', methods=['GET','POST'])
#def deletereviews():
 #   reviews=mongo.db.reviews.find()
  #  mongo.db.reviews.remove({'_id': ObjectId(review_id)})
   # return redirect(url_for('viewreviews'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)