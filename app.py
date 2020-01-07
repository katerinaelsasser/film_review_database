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

#linking the index
@app.route('/')
@app.route('/get_films')
def get_films():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)