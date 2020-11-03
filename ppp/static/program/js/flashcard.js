function unblur(){
  var flashcard = document.getElementById("flashcard");
  flashcard.classList.remove("blur");
  var vocab = document.getElementById("flashcard-vocab");
  vocab.style.display = "none";
}
