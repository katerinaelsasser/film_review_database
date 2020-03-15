//subscribe modal
var modal = document.getElementById("submodal");
var btn = document.getElementById("subscribebtn");
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

//login modal
var logmodal = document.getElementById("loginmodal");
var btn = document.getElementById("loginbtn");
var span = document.getElementsByClassName("close")[0];
btn.onclick = function() {
  logmodal.style.display = "block";
}
span.onclick = function() {
  logmodal.style.display = "none";
}
window.onclick = function(event) {
  if (event.target == logmodal) {
    logmodal.style.display = "none";
  }
}