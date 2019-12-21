import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Home page
@app.route('/')
def home_page():
        return render_template(
                'index.html',
                active='home',
                title="Home")

# Review page
@app.route('/review)
def review_page():
        return render_template(
                'review.html',
                active='review',
                title="Review")

if __name__ == '__main__':
        app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)