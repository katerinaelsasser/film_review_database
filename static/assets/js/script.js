function getMovies(film) {
  fetch('http://www.omdbapi.com/?i=tt3896198&apikey=8fb317f8')
    .then(res => res.json)
    .then(data => {
      console.log(data);
      data.Search.forEach(film => {
        let movieInfo = "
        <div class="row mb-2">
    <div class="col-md-4">
      <div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
        <div class="col p-4 d-flex flex-column position-static">
          
          <h3 class="mb-0">{{film.film_name}} ( {{film.film_year}} )</h3>
          <h5 class="mb-0">{{film.film_age}}</h5>
          <h5 class="mb-0">{{film.film_length}}</h5>
          <h6 class="mb-0">{{film.film_director}}</h6>
           <p class="card-text mb-auto">{{film.film_genre}}</p>

          <p class="card-text mb-auto">{{film.film_description}}</p>
          
        </div>
        <div class="col-auto d-none d-lg-block">
          <svg class="bd-placeholder-img" width="200" height="250" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"></rect><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>
        </div>
      </div>
    </div>
  </div>"}
        $('#movies').appendTo(movieInfo);
      });
    });
}