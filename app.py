# import section
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import os

#mongodb
app = Flask(__name__)
app.config[
    'MONGO_URI'] = 'mongodb+srv://kit_22:Nsos2015@filmreviews-dqtff.mongodb.net/test?retryWrites=true&w=majority'
app.config['MONGO_DBNAME'] = 'DataCentricLocksProject'
mongo = PyMongo(app)

#connecting the index file
@app.route('/')
@app.route('/index')
def index():
    context = mongo.db.Locks.find()
    return render_template('index.html', locks=context)

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)