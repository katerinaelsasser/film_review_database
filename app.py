import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'film_database'
app.config["MONGO_URI"] = 'mongodb+srv://kit_22:Milo0104@filmreviews-dqtff.mongodb.net/film_database?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_films')
def get_films():
    return render_template("films.html", films=mongo.db.films.find())


@app.route('/add_film')
def add_film():
    return render_template('addfilm.html',
                           categories=mongo.db.categories.find())


@app.route('/insert_film', methods=['POST'])
def insert_film():
    films =  mongo.db.films
    films.insert_one(request.form.to_dict())
    return redirect(url_for('get_films'))


@app.route('/edit_film/<film_id>')
def edit_film(film_id):
    the_film =  mongo.db.films.find_one({"_id": ObjectId(film_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editfilm.html', film=the_film,
                           categories=all_categories)


@app.route('/update_film/<film_id>', methods=["POST"])
def update_film(film_id):
    films = mongo.db.films
    films.update( {'_id': ObjectId(film_id)},
    {
        'film_name':request.form.get('film_name'),
        'category_name':request.form.get('category_name'),
        'film_description': request.form.get('film_description'),
        'due_date': request.form.get('due_date'),
        'is_urgent':request.form.get('is_urgent')
    })
    return redirect(url_for('get_films'))


@app.route('/delete_film/<film_id>')
def delete_film(film_id):
    mongo.db.films.remove({'_id': ObjectId(film_id)})
    return redirect(url_for('get_films'))


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)