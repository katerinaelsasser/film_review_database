# FRATES - Data Centric Development Project

FRATES is a website created for movie lovers to find movies to watch and to also leave a review for movies so other users of the website can see what others think of the movie.
The aim of the website should hold data of of movies/reviews as well as being easy to use and to add to the database.

## UX

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
As a user, I want to be able to navigation between the pages easily.
As a user, I want to see a clean layout of all the information.
As a user, I want to see images of the movies as well as the posters.
As a user, I want to see information about the movies.
As a user, I want to be able to review movies.
As a user, I want to be able to view other reviews that other users have added.
As a site owner, I want to be able to access data on the website that other users cannot.
As a site owner, I want to have access to add and editing movies.
As a site owner, I want to be able to delete movies and reviews if needed.

### Flow Chart
Taking the goals in mind of what the website should be, i started to plan out a flow chart of the whole of the website. The flow chart became would help create the website as this would show me what i would need to include on pages and how i would display some of the pages. For example: if a form when submited would send a user to a page that would have buttons leading to other pages on the website. So when creating the website, I would need to create buttons linking to other pages.

Click here to view the flow chart.

### Visuals
Other than data, visuals will be a big part of the website as this will be encouraging users to use the website. Posters of movies will be features on the website and as well as this, imagergy from movie scenes will also be featured throughout the website. 

### Wireframes
After finding the goals, research and having a flow chart, I started to put together wireframs for the website. I created multiple versions of them (one for mobile view and the other for medium/laptop view). This would help when creating it as I would follow this as guidelines.

wireframes
* Main pages
* forms
* Modals


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