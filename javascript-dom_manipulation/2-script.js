// Au clic, ajoute la classe CSS 'red' au header (ex. appliquer un style via classe).
const headerElement = document.querySelector('header');
const idButton = document.querySelector('#red_header');
idButton.addEventListener('click', function() {
  headerElement.classList.add('red')
})