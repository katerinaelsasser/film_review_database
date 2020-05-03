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
@app.route('/deletereviews/<review_id>', methods=['GET','POST'])
def deletereviews():
    reviews = mongo.db.reviews.find()
    mongo.db.reviews.remove({'_id': ObjectId(reviews_id)})
    return redirect(url_for('deletereviews'))

#Edit films
@app.route('/editform/<film_id>', methods=["GET"])
def editform():
    films=mongo.db.films.find()
    films=mongo.db.films.find_one({"film_id": ObjectId(film_id)})
    print(films)
    mongo.db.films.update( {'_id': ObjectId(film_id)},
    {
        'film_name':request.form.get('film_name'),
        'film_director': request.form.get('film_director'),
        'film_description': request.form.get('film_description'),
        'film_genre':request.form.get('film_genre'),
        'film_year':request.form.get('film_year'),
        'film_age':request.form.get('film_age'),
        'film_poster':request.form.get('film_poster'),
    })
    return render_template("pages/editform.html", films=films)

#Add Movie
@app.route('/addfilm', methods=['GET'])
def addfilm():
    return render_template("pages/addfilm.html")

@app.route('/insertfilm', methods=['POST'])
def insertfilm():
    films =  mongo.db.films
    films.insert_one(request.form.to_dict())
    return redirect(url_for('viewfilms'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)