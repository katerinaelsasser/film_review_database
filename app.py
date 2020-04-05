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
#@app.route('/view/movies/'<imdbID>)
#def movieID():
    #return render_template("pages/individualfilm.html")

#addreviews page
@app.route('/addreviews', methods=['GET'])
def addreviews():
    return render_template("pages/addreviews.html")

@app.route('/insertreview', methods=['POST'])
def insertreview():
    reviews =  mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('viewreviews'))

#login page   
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form.get['username'] != 'admin' or request.form.get['password'] != 'password':
            error = 'Invalid Username or Password. Please try again.'
        else:
            return redirect(url_for('userhome'))
    return render_template("pages/login.html", error=error)
    
#user home page
@app.route('/userhome', methods=['GET'])
def userhome():
    return render_template("pages/userhome.html")

#Delete reviews
@app.route('/deletereviews')
def deletereviews():
    reviews=mongo.db.reviews.find()
    print(reviews)
    return render_template("pages/deletereviews.html", reviews=reviews)

@app.route('/deletereviews/<review_id>')
def removereview(review_id):
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('deletereviews'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)