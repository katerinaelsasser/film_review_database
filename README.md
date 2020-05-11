# FRATES - Data Centric Development Project

FRATES is a website created for movie lovers to find movies to watch and to also leave a review for movies so other users of the website can see what others think of the movie.
The aim of the website should hold data of of movies/reviews as well as being easy to use and to add to the database.

Users of the website can browser information about these movies/reviews and also can add reviews to the movies.
The site owner must be able to adjust data that is shown on the website easily. Meaning if they see reviews/movies that they don't want on the website, they can easily remove if needed. As well as this, they must be able to edit movie information if there is an error in the cluser of infomation.

## UX
### Surface
I put together mock ups of what the database would look like. For the two mockups I have created two versions: a mobile and a laptop version. The first mockup is of what the main page containing the database of the movies. In the second mockups, this is for the page where users can input info to the database.

#### wireframes
### Page 1
[Mobile Version](https://github.com/katerinaelsasser/movie_review_database/blob/master/images/mockups/mobile_mockup_1.jpg)

[Laptop Version](https://github.com/katerinaelsasser/movie_review_database/blob/master/images/mockups/laptop_mockup_1.jpg)

### Page 2
[Mobile Version](https://github.com/katerinaelsasser/movie_review_database/blob/master/images/mockups/mobile_mockup_2.jpg)

[Laptop Version](https://github.com/katerinaelsasser/movie_review_database/blob/master/images/mockups/laptop_mockup_2.jpg)

### Strategy
The aim of this website is so users can find movies and the site owner can earn money from users buying the movies. The information and the images that will be on the page must link to the movies in the database. The infomation in the database must be inform the user about the movies.

### Structure
The website will be structured so there is a link between two pages which will both be linked to the database. The website must be structured so that users can buy the movies.

### Skeleton
The database will be the skeleton of this website as both pages will link to the database as this is what the site owner wants the website to have the main focus on it.

### Scope
Before creating the website, I put together all the infomation that the site owner wants to be din the database. I also found images of the movie posters that will be the icon of the movies.

### User Stories
As a user, I want to be able to navigation between the pages easily.
As a user, I want to see a clean layout of all the information.
As a user, I want to see images of the movies.
As a user, I want to see information about the movies.
As a user, I want to be able to review the movies.
As a user, I want to be able to buy the movie.

## Features

### Existing Features
### Features Left To Implement
## Technologies Used
HTML
CSS
Javascript
JQuery
Flask
Python
Bootswatch
GitPod
PyMongo
## Testing
The user stories that I have made at the beginning will help with testing as well as being a check list.

### Tests Done To Create Website
Add fetch code on the js file that will link to the JSON.
Test the code
Add " around the data and the title of the rows
Testing the code
Data appears on the map

## Information Architecture
The information collected and stored in this website database. I have used MongoDB which holds data for reviews that has been submitted. 

### User Collection

| Title	    | Key in db | form validation type | Data type |
|-----------|:---------:|:--------------------:|:---------:|
|Username   |username   |                      |           |
|Password   |password   |                      |

### Review Collection

| Title	    | Key in db | form validation type | Data type |
|-----------|:---------:|:--------------------:|:---------:|
|_id        |_id        |None                  |Object Id  |
|IMDB_id    |imdb_id    |                      |
|movie Title |movie_name  |                      |string     |
|Star Rating|movie_star  |                      |           |
|Review     |movie_review|                      |string|
|Nickname   |nickname   |                      |      |


## Deployment
The website was deployed from the master branch and has been hosted on the GitHub pages. When I add a new commit to this master website, it will be automatically updated. I deployed it by doing the following steps:

Going on to my GitHub page
Clicking on the repository that I would like to deploy
Clicking on the tab called Settings
Scrolling all the way down to the section on settings called GitHub Pages
Clicking the dropdown button that has the title Source
Change the source from None to Master Branch
## How to run this project locally
The following steps are how you can clone this project from GitHub.

Head over to the repsositpory for the project. In this case it would be this link.
Underneath the name of the repository, there is a coloured button called Clone or Download.
When this button is clicked it will pop up with a link. Copy the URL for the repository.
In the local IDE open Git Bash
Where the clone directory is to be made, change the current working directory.
Type in the git clone and then insert the URL that has been copied.
## Credits
### Content

### Media
All images were taken from Pixabay and Unsplash.

### Acknowledgements

#### Please note that this is for educational use only.