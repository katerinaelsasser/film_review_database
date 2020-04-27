//search bar
function filmSearch() {
    var userSearchBar = document.getElementById('filmSearchBar').value;
    $('#moviesDIV').empty();
    fetch('https://www.omdbapi.com/?apikey=fe2afef6&s='+userSearchBar+'&type=movie')
    .then(res => res.json())
    .then(data => {
console.log(data.Search);
      data.Search.forEach(movie => {
console.log(movie.Title);
        let moviePreview =
        `<div class="col-md-3 film-card film-effect">
        <div class="card border-0 shadow">
        <a href="/view/movies/${movie.imdbID}">
            <img src="${movie.Poster}" class="card-img-top" alt="movie-poster"></a>
            <h4 class="text-center film-title">${movie.Title}</h4>
            </div>`;
        $('#moviesDIV').append(moviePreview);
      });
    });
}

$("#filmSearchBar").change(function () {
    filmSearch();
});

const userSearchBar = $("#filmSearchBar")

//individual page
function filmview() {
var movie_id = document.getElementById('movie_id').value;
 fetch('https://www.omdbapi.com/?apikey=fe2afef6&i='+movie_id)
 .then(res => res.json())
    .then(data => {
console.log(data.Search);
      data.Search.forEach(movie => {
console.log(movie.imdbID);
        let movieInfo =   
        `<div class="col-md-9 col-lg-8 mx-auto">
              <h3 class="login-heading mb-4">${movie.Title}</h3>
                <div>
                ${movie.Year} | ${movie.Rating}
                </div>
                <div>
                ${movie.Genre} | ${movie.Runtime}
                </div>
                <div>
                Director : ${movie.Director}
                </div>
                <div>
                ${movie.Plot}
                </div>
            </div>
            <div class="d-none d-md-flex col-md-4 col-lg-6 bg-image">
    <img src="${movie.Poster}">
    </div>`;
        $('#Film_ID').append(movieInfo);
      });
    });
}

