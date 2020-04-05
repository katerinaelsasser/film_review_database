//search bar
function bob(userSearch) {
    fetch('https://www.omdbapi.com/?j=tt3896198&apikey=8f317f8&plot=ful=$(userSearch)&type=movie')
    .then(res => res.json())
    .then(data => {
      console.log(data);
      data.Search.forEach(element => {
        let movieInfo = `
        '<div class="col-md-3 film-card">
        <div class="card border-0 shadow">
            <img src="{poster}" class="card-img-top" alt="movie-poster">
            <p>"${movie.Title}"</p>
            </div>`;
        $('#moviesDIV').appendTo(movieInfo);
      });
    });
}