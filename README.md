# FRATES - Data Centric Development Project

FRATES is a website created for movie lovers to find movies to watch and to also leave a review for movies so other users of the website can see what others think of the movie.
The aim of the website should hold data of of movies/reviews as well as being easy to use and to add to the database. The site owner of the website wants the user to review movies that are in the database.

# UX

### Goals
Users of the website can browser information about these movies/reviews and also can add reviews to the movies.
The site owner must be able to adjust data that is shown on the website easily. Meaning if they see reviews/movies that they don't want on the website, they can easily remove if needed. As well as this, they must be able to edit movie information if there is an error in the cluser of infomation.

This website should be suitable, easy to use and visually appealing for both user and site owner. The navigation should be able to access all pages (one navbar for all users of the website and the other for the site owner to use when accessing the whole database).

The data that the site owner has access to must be easy to use, easy to add/remove/update if required. The data is the main part of the website which means the website must always have a direction to a page that has the data on. For example: If a user leaves a review, they must be redirected to a page where they can access to see the movies or see/add reviews on the website.

The whole site has to be responsive when adjusted to all devices (small, medium and large). This means that when created, all devices must thought about when adding features and should be adaptable. 

### Research
When researching similar websites that contain movie/review data (such as RottenTomato and IMDB), I noticed that the website was appealing to look at and was easy to use. The data was displayed clear and was easy to read/access. Having this research in my mind, all the data throughout the website needs to be the exact same. If the website isn't users won't want to use it. The website needs to have imagergy that would be appealing for users, instead of having a plan website.

### Data 
Before thinking about what the website is going to look like, I need to think about what data is going to be put on the website. The main things that is required is data about the movies (which includes poster, title, plot, year, etc) and the review data (this would be gradually added by users of the website). 

### User Stories
* As a user, I want to be able to navigation between the pages easily.
* As a user, I want to see a clean layout of all the information.
* As a user, I want to see images of the movies including the posters.
* As a user, I want to see information about the movies.
* As a user, I want to be able to review movies.
* As a user, I want to be able to view other reviews that other users have added.
* As a site owner, I want to be able to access data on the website that other users cannot.
* As a site owner, I want to have access to add and editing movies.
* As a site owner, I want to be able to delete movies and reviews if needed.

### Flow Chart
Taking the goals in mind of what the website should be, i started to plan out a flow chart of the whole of the website. The flow chart became would help create the website as this would show me what i would need to include on pages and how i would display some of the pages. For example: if a form when submited would send a user to a page that would have buttons leading to other pages on the website. So when creating the website, I would need to create buttons linking to other pages.

[Click here](https://raw.githubusercontent.com/katerinaelsasser/film_review_database/master/wireframes/flow-chart-data-centric-2020.jpg) to view the flow chart.

### Visuals
Other than data, visuals will be a big part of the website as this will be encouraging users to use the website. Posters of movies will be features on the website and as well as this, imagergy from movie scenes will also be featured throughout the website. 

### Wireframes
After finding the goals, research and having a flow chart, I started to put together wireframs for the website. I created multiple versions of them (one for mobile view and the other for medium/laptop view). This would help when creating it as I would follow this as guidelines.

wireframes
* Main pages
* * [Laptop version](https://raw.githubusercontent.com/katerinaelsasser/film_review_database/master/wireframes/main-page-laptop.jpg)
* * [Mobile Version](https://raw.githubusercontent.com/katerinaelsasser/film_review_database/master/wireframes/main-page-mobile.jpg)
* Forms
* * [Laptop version](https://raw.githubusercontent.com/katerinaelsasser/film_review_database/master/wireframes/form-laptop.jpg)
* * [Mobile Version](https://raw.githubusercontent.com/katerinaelsasser/film_review_database/master/wireframes/form-mobile.jpg)
* Modals
* * [Laptop version](https://raw.githubusercontent.com/katerinaelsasser/film_review_database/master/wireframes/modal-laptop.jpg)
* * [Mobile Version](https://raw.githubusercontent.com/katerinaelsasser/film_review_database/master/wireframes/modal-mobile.jpg)


# Features
## Existing Features
### All Pages
 * Slideshow - Throughout the website, there is a carousel of images. This is for the visual side of the website as this is appealing for users. The images used are images from scenes of movies that are in the database.
### Home Page
* Buttons - The buttons on the home page take the user/site owner to use to access other pages on the website.
* About - There is a section at the bottom of the page that talks about the website and why it was made.
* Login Form - This form is for the site owner so they can access the admin side of the website. They access pages user of the website cannot access. I put this on the index page so the site owner can go straight to the admin side if they want to edit, add or delete data.
### View movies
* Data - The data on this page is the data of the movies. This is linked to the mongodb collection called "movies". This collection holds the infomation of each movie.
* Film Cards - The film cards display the poster and the title of the each movie that is in the collection. This is a preview for the user to click on. This is linked to mongodb.
* Modals - The modal is linked to mongodb and displays infomation of the movies. This also has buttons at the bottom that link to other pages that encourages users to either view reviews that have been submitted or add reviews. 
### View reviews
* Data - The data on this page is the data of the reviews that users have submitted. This is linked to the mongodb collection called "reviews". This collection holds the infomation of each review (which includes star rating and the text review).
* Button - There is a button on the reviews that encourages users to go to the add review.
### Add reviews
* Form - The review form is connected to the mongodb collection called "reviews". When a user submits a review, it will be sent to the collection and the user will be sent to the submit page. The form is also linked to the "movies" collection on the dropdown, this is so users can find the movie that they want to review.
### Login
* Login Form - This form is for the site owner so they can access the admin side of the website. They access pages user of the website cannot access.
* About - There is a section at the bottom of the page that talks about the website and why it was made.
### User Home
* Buttons - The dashboard on the user page acts as another navbar, all pages of the admin side are displayed here and linked to. 
### Add movies
* Form - The movie form is connected to the mongodb collection called "movies". When the site owner submits a movie, the data will be sent to the collection and the site owner will be sent to the submit page.
### Submit Pages (Reviews/Movies)
* Buttons - When the user/site owner submits data to mongodb, they will be sent to the subtmit page. This is where they will be given an option to use/go to other parts of the website. When the user send a review, they will given a choice if they want to see other movies, view other reviews or add another review. When the site owner submits a movie, they will be given a choice of viewing the movies, add another movie, add a review or view the reviews.
### Edit/Delete movies
* Data - The data on this page is the data of the movies. This is linked to the mongodb collection called "movies". This collection holds the infomation of each movie.
* Button - The delete button is connected to the mongodb collection "movies", this is used for when the site owner wanted to delete a movie. The edit button is linked to the modal on the page so the site owner can adjust the data if they have made an error.
* Film Cards - The film cards display the poster and the title of the each movie that is in the collection. This is a preview for the site owner to click on. This is linked to mongodb.
* Modals - The modal is linked to mongodb and displays infomation of the movies in a form. This is so they can adjust the data. 
### Delete reviews
* Data - All the reviews are displayed on the page, showing all the data from each review.
* Button - The delete button is connected to the mongodb collection "reviews", this is used for when the site owner wanted to delete a review.

### Features Left To Implement
Other time users will use the website more and the site owner will add more data to the collection. Over this time, the website can develop more.
* User Logins - A user login can be created so users can have a collection of review that have added and names/nicknames can be shown on the reviews.
* Movie data - As the collection of movies grows, more data for each of the movies can be added to it. Such as actors, writers, pictures from the movie.
* Movie Review Page - A page for each movie will have the infomation and all the reviews collected and displayed on it.
* Filters - Filters can be added to both movie/review pages so users can filter down on the collection. For example: if users want to see reviews for a specific movie, they would click on a button which will filter down all the reviews for that movie.

## Information Architecture
For this website, I have collected infomation and have stored in a database. I have used MongoDB to be the database that stores this. Throughout this website, there are two collections that have been used, Movies and Reviews. 

### Movie Collection

| Title	    | Key in db | form validation type | Data type |
|-----------|:---------:|:--------------------:|:---------:|
|_id        |_id        | None                 |Object Id  |
|Movie Title|  title    |  text                |string     |
|Year Release|  year    |   text               |string     |
|Age Rating |  rated    |  dropdown            |string     |
|Genre      |  genre    |  text                |string     |
|Director   | director  |  text                |string     |
|Movie Plot |  plot     |text                  |string     |
|Movie Poster| poster   |  text                |string     |


### Review Collection

| Title	    | Key in db | form validation type | Data type |
|-----------|:---------:|:--------------------:|:---------:|
|_id        |_id        |None                  |Object Id  |
|Movie Title|movieName  |dropdown              |string     |
|Star Rating|movieStar  |  dropdown            | string    |
|Review     |movieReview|text                  |string     |


# Technologies Used
Throughout the website, I have used lots of tools and libaries to help create the features on the website. Below is the list of all the things I have used.

HTML
CSS
Python
Flask
Heroku
JavaScript
JQuery
MongoDB
Jasmine
Bootswatch
Bootstrap
Git
PyMongo
Jshint

# Testing
When I was testing the website, there were different things I have checking. The user stories that I created at the beginning of this project as a big part of the testing as this was the goal of the whole website and was expected from users and the site owner. The other way I was testing was checking the code was vaildated. Below is how I did the test for the whole of this project.

## User Stories
The user stories that I have made at the beginning will help with testing as well as being a check list for the website.
### Users of FRATES
> As a user, I want to be able to navigation between the pages easily.

I have created two navigation bars (one for the user and one for the site owner) which links for the appropriate user. Both navigation bars are linked to the appropriate pages and are located at the top of the website. The nav bar for the site owner was created so that they can have full access to pages for the admin (for example: when adding/editing/deleting data that the site owner doesn't want a user to be able to access).

> As a user, I want to see a clean layout of all the information.

All information has been present clearly by not bunching it up together. I have broken down information so that users can understand it. The colour scheme was also taken into account as this would also be a way of creating clear infomation. 

> As a user, I want to see images of the movies as well as the posters.

Through out the website, I have used images from movies including the posters. The posters are presented on the view movies page as well as the edit/delete movies page. On all pages, I have used images from movies in a slideshow. 

> As a user, I want to see information about the movies.

The infomation about the movies have been used in a modal as I thought that was a clear way of displaying this data. As well as this, data has been used for previews for users to click on it access the modals.

> As a user, I want to be able to review movies.

I have created a page that has a review form. The form is linked to the Review collection and is also connected to the Movie collection (this is so users can click on the movie title they would like to review). Throughout the website, there are buttons that link the users to the review page as this is what the site owner wants the aim of this website to be.

> As a user, I want to be able to view other reviews that other users have added.

I have created a view all review page which can be accessed on pages as well as in the navigation bar.

### Admin of FRATES
> As a site owner, I want to be able to access data on the website that other users cannot.

I have created a seperate section (after logging in) for the site owner to access pages that users wouldn't be able to access. These are the add/edit/delete movies pages and the delete reviews page.

> As a site owner, I want to have access to add and editing movies.

I have created two pafes for this (Add Movies and Edit/Delete Movies). I wanted to keep them seperate so I can make this easy for the site owner to understand and read. The Add Movies is a page with a form (similar layout to the review) and the Edit/Delete Movies has a edit button which is a link to a modal. On the modal, I have presented it in the Add Movie form as I thought this would be a clear way of showing the data.

> As a site owner, I want to be able to delete movies and reviews if needed.

I have created two pages for these features (Edit/Delete Movies and View/Delete Movies). I have create a red delete button for these features, the buttons are connected to the two collections so they will be removed from them.

## Code Testing
I have used websites to test the data to see if there any errors in it. I have used them frequently throughout the process of the website. I have used three services that have helped with the HTML, CSS, Python and JavaScript.
### HTML/CSS
The HTML and CSS code have been texted on the W3C Markup Validation (for the HTML code) and W3C CSS Validation (for the CSS code). When errors have come up, I have adjusted where it is needed.
### Python
For testing the python that I had throughout the pages, I used PythonBuddy. When I put in my code, it would say where the errors I had, I then would adjust if necessary.
### JavaScript
My JavaScript has been tested JSHint and Jasmine. As this project wasn't based on my JavaScript, I didn't want to have a lot of JS code. This meant that I didn't have a lot to test. Like the other code vailidators, if a error came up, I adjusted where it was needed.
### Tests Done To Create Website
Test the code
Add " around the data and the title of the rows
Testing the code
Data appears on the map

# Deployment
## Deploying to Heroku
The website was deployed and hosted through Heroku. I have connected this through my terminal. I have used code that has been supplied by heroku on their 'Deploy' tab. 

These were the steps that I took:

* A `requirement.txt` file was created using the command on my terminal `pip freeze > requirement.txt`
* I then created a `Procfile` which as was also created on my terminal using `echo web: python app.py > Procfile`
* Putting `git add` followed by `git commit` and then `git push` to put my new files on GitHub
* On my Heroku account, press the **New** located on the dashboard. Give it a name and select the region to be **Europe**
* When this is created, go to the **Delpoy** tab. Under the section **Deployment method**, select out of the three options **GitHub**. 
* Choose the link to your GitHub repository. In this case, it would be this [link](https://github.com/katerinaelsasser/film_review_database).
* After this is connected, head over to the **Settings** tab.
* Go to the section called **Reveal Config Vars**.
* Fill in the following into the correct fields.

| Key	    | Value | 
|-----------|:---------:|
|IP     |  0.0.0.0      |
|MONGO_DBNAME|#`INSERT NAME OF DATABASE OF MONGODDB`#  |
|MONGO_URI|#`INSERT URI OF MONGODDB`#|
|PORT|8080|

The `MONGO_DBNAME` and `MONGO_URI` are supplied through MongoDB account (under `connect` on your MongoDB database).

* In the heroku dashboard, click **Deploy**. Under the **Manual Deployment** section, select the branch that you want to connect to.
* Once selected click on the button **Deploy Branch**

When these steps have been followed, the website will be successfully deployed.

#### Deploying Changes To My Website

>$ heroku login

This is code that links to my account on heroku. When this is added to the terminal, I put in my login details.

> $ heroku git:clone -a films-and-reviews

>$ cd films-and-reviews

This code was for cloning my repository to my local machine.

>$ git add .

>$ git commit -m "##########"

>$ git push heroku master

This code was for when I deployed changes of my website. I would use *git add .* , followed by *git commit -m ""*  (in the quotation marks, I would put in a snippet of what I did), then I would put in *git push heroku master* (this would be sent to both my git repository as well being sent to heroku).

When I add a new commit to this master website, it will be automatically updated.

## Credits
### Content
Information about movies in the database were sourced from [IMDB](https://www.imdb.com/) and reviews in the database were created by myself.
### Media
All images were taken from [IMDB](https://www.imdb.com/).

### Acknowledgements

This website was inspired by [IMDB](https://www.imdb.com/) and [Rotten Tomatoes](https://www.rottentomatoes.com/). Movies that were included on my page were the movies that I have watched over the last year. My mentor, Simen Daehlin, inspired the movie infomation to be connected to the view movie page.
#### Please note that this is for educational use only.