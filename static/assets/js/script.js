//film form (genre modal)
var modal = document.getElementById("myModal");
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];
btn.onclick = function() {
  modal.style.display = "block";
}
span.onclick = function() {
  modal.style.display = "none";
}
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

//search bar
function bob(userSearch) {
    fetch('https://www.omdbapi.com/?j=tt3896198&apikey=8f317f8')
    .then(response=>response.json())
    .then(searchResults=>{
        searchResults.Search.ForEach(movie=>{
        if(movie.Poster ==="N/A")(
        let poster = "assets/noPOSTER.jpg"
        )else{
            poster = movie.Poster
        }
    $("#movieDIV").append(
        '<div class="col-md-3 film-card">
        <div class="card border-0 shadow">
            <img src="{poster}" class="card-img-top" alt="movie-poster">
            <p>"${movie.Title}"</p>
            </div>'
    );
    });
});
}
