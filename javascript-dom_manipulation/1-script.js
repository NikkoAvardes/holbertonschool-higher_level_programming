// Ajoute un gestionnaire de clic qui colore le <header> en rouge.
// Montre l'utilisation basique d'un event listener.
const headerElem = document.querySelector('header');
const idButton = document.querySelector('#red_header');
idButton.addEventListener('click', function() {
  headerElem.style.color = '#FF0000'
})