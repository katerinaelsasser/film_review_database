//info modal

var modal = document.getElementById("infoModal");
var btn = document.getElementById("infoBtn");
btn.onclick = function() {
  modal.style.display = "block";
}
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

//review modal

var reviewModal = document.getElementById("reviewModal");
var reviewBtn = document.getElementById("reviewBtn");
reviewBtn.onclick = function() {
  reviewModal.style.display = "block";
}
window.onclick = function(event) {
  if (event.target == reviewModal) {
    reviewModal.style.display = "none";
  }
}

//edit modal

var editModal = document.getElementById("editModal");
var editBtn = document.getElementById("editBtn");
editBtn.onclick = function() {
  editModal.style.display = "block";
}
window.onclick = function(event) {
  if (event.target == editModal) {
    editwModal.style.display = "none";
  }
}

//close modal

var span = document.getElementsByClassName("close")[0];
span.onclick = function() {
  modal.style.display = "none";
}