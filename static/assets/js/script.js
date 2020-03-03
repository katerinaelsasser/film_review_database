function getanswers(film) {
fetch("mongodb+srv://kit_22:MONGO_URI@filmreviews-dqtff.mongodb.net/test?retryWrites=true&w=majority)
.then(res => res.json())
    .then(data => {
      console.log(data);
      data.Search.forEach(element => {
 let movieInfo = "<div><div id="${film._ID}">
        <div>
          <img src="${film.film_poster}">
          <span class="card-title">${film.film_name}</span>
        </div>";
        $('#movies').appendTo(movieInfo);
      });
    });
}
}
