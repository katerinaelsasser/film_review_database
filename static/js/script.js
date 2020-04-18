//search bar
function filmSearch(userSearcBar) {
    fetch('https://www.omdbapi.com/?apikey=8fb317f8&s='+userSearchBar+'&type=movie')
    .then(res => res.json())
    .then(data => {
document.getElementById('userSearchBar').value;
console.log(data.Search);
      data.Search.forEach(movie => {
console.log(movie.Title)
        let movieInfo =
        `<div class="col-md-3 film-card">
        <div class="card border-0 shadow">
        <a href="/view/movies/${movie.imdbID}">
            <img src="${movie.Poster}" class="card-img-top" alt="movie-poster"></a>
            <p>${movie.Title}</p>
            </div>`;
        $('#moviesDIV').append(movieInfo);
      });
    });
}
const userSearchBar = $("#filmSearchBar");
const searchButton = $("#searchButton");

