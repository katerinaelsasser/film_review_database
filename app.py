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
@app.route('/addreviews', methods=['GET'])
def addreviews():
    return render_template("pages/addreviews.html")

@app.route('/insertreview', methods=['POST'])
def insertreview():
    reviews =  mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('viewreviews'))

#addfilm page
@app.route('/addfilm', methods=['GET'])
def addfilm():
    return render_template("pages/addfilm.html")

@app.route('/insertfilm', methods=['POST'])
def insertfilm():
    films =  mongo.db.films
    films.insert_one(request.form.to_dict())
    return redirect(url_for('viewfilms'))

#login page
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if 'logged in' in session:
        return redirect(url_for('index.html'))
    
    if form.validate_on_submit():
        existing_user = mongo.db.users.find_one({'username': request.form['username']})
        if existing_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), 
            login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                session['logged in'] = True
                return redirect(url_for('index'))
    return render_template('login.html', form=form)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("pages/login.html")

@app.route('/loginform', methods=['POST'])
def loginform():
    return redirect(url_for('userhome'))

#user home page
@app.route('/userhome')
def userhome():
    return render_template("pages/userhome.html")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)