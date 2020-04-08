# FRATES - Data Centric Development

FRATES is a website that is created for users to find films and to review them.

This project is a website database full of information about films. Users of this website can browser information about these films and also can add reviews to the films.
External Users must be able to find films and the site owner must be able to earn money on each film purchased.

## UX
### Surface
I put together mock ups of what the database would look like. For the two mockups I have created two versions: a mobile and a laptop version. The first mockup is of what the main page containing the database of the movies. In the second mockups, this is for the page where users can input info to the database.

#### wireframes
### Page 1
[Mobile Version](https://github.com/katerinaelsasser/film_review_database/blob/master/assets/images/mockups/mobile_mockup_1.jpg)

[Laptop Version](https://github.com/katerinaelsasser/film_review_database/blob/master/assets/images/mockups/laptop_mockup_1.jpg)

### Page 2
[Mobile Version](https://github.com/katerinaelsasser/film_review_database/blob/master/assets/images/mockups/mobile_mockup_2.jpg)

[Laptop Version](https://github.com/katerinaelsasser/film_review_database/blob/master/assets/images/mockups/laptop_mockup_2.jpg)

### Strategy
The aim of this website is so users can find films and the site owner can earn money from users buying the films. The information and the images that will be on the page must link to the films in the database. The infomation in the database must be inform the user about the films.

### Structure
The website will be structured so there is a link between two pages which will both be linked to the database. The website must be structured so that users can buy the films.

### Skeleton
The database will be the skeleton of this website as both pages will link to the database as this is what the site owner wants the website to have the main focus on it.

### Scope
Before creating the website, I put together all the infomation that the site owner wants to be din the database. I also found images of the movie posters that will be the icon of the films.

### User Stories
As a user, I want to be able to navigation between the pages easily.
As a user, I want to see a clean layout of all the information.
As a user, I want to see images of the movies.
As a user, I want to see information about the films.
As a user, I want to be able to review the movies.
As a user, I want to be able to buy the film.

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

### Review Collection

| Title	    | Key in db | form validation type | Data type |
|-----------|:---------:|:--------------------:|:---------:|
|_id        |_id        |None                  |Object Id  |
|IMDB_id    |imdb_id    |                      |
|Film Title |film_name  |                      |string     |
|Star Rating|film_star  |                      |           |
|Review     |film_review|                      |string|
|Nickname   |user_name  |                      |      |


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