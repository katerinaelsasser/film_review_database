function getanswers(film) {
$.get("http://www.omdbapi.com/?i=tt3896198&apikey=8fb317f8")
    let rawstring=JSON.stringify(rawdata);
    data=JSON.parse(rawstring)
    let title = data.Search[0].Title;
    let year = data.Search[0].Year;
    let posterurl = data.Search0[0].Poster;
    document.getElementById('film-results').innerHTML="
    "<div>"+"<img scr="+posterurl+"><h3>"+title+" ( "+year+" )</h3>";
 }
