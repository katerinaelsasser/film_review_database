import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'film_database'
app.config["MONGO_URI"] = os.getenv(
                        'MONGO_URI', 
                        'mongodb+srv://kit_22:Nsos2015@filmreviews-dqtff.mongodb.net/test?retryWrites=true&w=majority')

mongo = PyMongo(app)

# Home
@app.route('/')
def home_page():
        return render_template(
                'index.html',
                active='home',
                title="Home")

# Review
@app.route('/review)
def review_page():
        return render_template(
                'review.html',
                active='review',
                title="Review")

if __name__ == '__main__':
        app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)