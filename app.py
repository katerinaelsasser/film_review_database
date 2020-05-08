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
@app.route('/movies/view', methods=['GET'])
def viewmovies():
    movies = mongo.db.movies.find()
    print(movies)
    return render_template("pages/viewfilms.html", movies=movies, TitlePage="Find A Movie")

#Leave review

#Add Reviews
@app.route('/review/add')
def addreview():
    return render_template("pages/addreview.html", TitlePage="Leave A Review")

@app.route('/insertreview', methods=['POST'])
def insertreview():
    movies =  mongo.db.movies
    print(movies)
    reviews =  mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('reviewsubmited')), render_template (movies=movies)

@app.route('/review/add/submitted')
def reviewsubmited():
    return render_template("pages/added.html", TitlePage="Leave A Review")

#login page   
@app.route('/login')
def login():
    return render_template("pages/login.html", TitlePage="Login")
    
#user home page
@app.route('/dashboard')
def userhome():
    return render_template("pages/userhome.html", TitlePage="Admin")

#View All Reviews
@app.route('/review/view', methods=['GET','POST'])
def viewreviews():
    reviews = mongo.db.reviews.find()
    print(reviews)
    return render_template("pages/viewallreviews.html", reviews=reviews, TitlePage="View All Reviews")

#Edit films
@app.route('/movies/edit', methods=["GET"])
def editmovies():
    movies = mongo.db.movies.find()
    print(movies)
    return render_template("pages/edit.html", movies=movies , TitlePage="Edit/Delete Movies")

@app.route('/movies/edit/<film_id>', methods=["POST"])
def updatemovies(movies_id):
    mongo.db.movies.update( {'_id': ObjectId(movies_id)},
    {
        'title':request.form.get('title'),
        'director': request.form.get('director'),
        'plot': request.form.get('plot'),
        'genre':request.form.get('genre'),
        'year':request.form.get('year'),
        'rating':request.form.get('rating'),
        'poster':request.form.get('poster'),
    })
    return redirect(url_for('editmovies'))

@app.route('/movies/edit/<film_id>')
def removemovie(movies_id):
    mongo.db.movies.remove({'_id': ObjectId(movies_id)})
    return redirect(url_for('editmovies'))

#Add Movies
@app.route('/movies/add')
def addmovie():
    return render_template("pages/addfilm.html")

@app.route('/insertmovie', methods=['POST'])
def insertmovies():
    movies =  mongo.db.movies
    movies.insert_one(request.form.to_dict())
    return redirect(url_for('viewmovies'))  


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)