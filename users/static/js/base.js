// When the user scrolls ,e xecute myFunction
window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar");

// navbar offset position
var sticky = navbar.offsetTop;

// Add and remove sticky clss
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

// autogrow height of textarea

$('.post').css('overflow', 'hidden').autogrow()