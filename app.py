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

#Add review
@app.route('/reviews/add', methods=['GET'])
def addreview():
    movies =  mongo.db.movies.find()
    print(movies)
    return render_template("pages/addreview.html", movies=movies, TitlePage="Leave A Review")

@app.route('/insertreview', methods=['POST'])
def insertreview():
    reviews =  mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('reviewsubmited'))

@app.route('/reviews/add/submitted')
def reviewsubmited():
    return render_template("pages/submitedrev.html", TitlePage="Leave A Review")

#View Reviews page
@app.route('/reviews/view', methods=['GET'])
def viewreviews():
    reviews = mongo.db.reviews.find()
    print(reviews)
    return render_template("pages/viewallreviews.html", reviews=reviews, TitlePage="View Reviews")

#Login page   
@app.route('/login')
def login():
    return render_template("pages/login.html", TitlePage="Login")
    
#(User) Home page
@app.route('/user')
def userhome():
    return render_template("pages/userhome.html", TitlePage="Admin")

#(User) View/Delete Reviews
@app.route('/user/reviews/view', methods=['GET','POST'])
def userreviews():
    reviews = mongo.db.reviews.find()
    print(reviews)
    return render_template("pages/deletereviews.html", reviews=reviews, TitlePage="View/Delete Reviews")

@app.route('/user/reviews/view/<review_id>')
def removereview(review_id):
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('userreviews'))

#(User) Edit films
@app.route('/user/movies/edit', methods=['GET'])
def editmovies():
    movies = mongo.db.movies.find()
    print(movies)
    return render_template("pages/edit.html", movies=movies, TitlePage="Edit/Delete Movies")

@app.route('/user/movies/edit/update/<movie_id>', methods=['GET','POST'])
def updatemovies(movies_id):
    mongo.db.movies.update( {'_id': ObjectId(movie_id)},
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

@app.route('/user/movies/edit/delete/<movie_id>')
def removemovie(movie_id):
    mongo.db.movies.remove({'_id': ObjectId(movie_id)})
    return redirect(url_for('editmovies'))

#(User) Add Movies
@app.route('/user/movies/add')
def addmovie():
    return render_template("pages/addfilm.html", TitlePage="Add Movie")

@app.route('/insertmovies', methods=['POST'])
def insertmovies():
    movies =  mongo.db.movies
    movies.insert_one(request.form.to_dict())
    return redirect(url_for('moviesubmited'))  

@app.route('/user/movies/add/submitted')
def moviesubmited():
    return render_template("pages/submitedmov.html", TitlePage="Leave A Review")

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)