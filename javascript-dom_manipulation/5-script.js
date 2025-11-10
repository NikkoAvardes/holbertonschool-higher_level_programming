// Remplace le contenu HTML du header lorsqu'on clique sur le bouton.
const headerElement = document.querySelector('header');
const idButton = document.querySelector('#update_header');
idButton.addEventListener('click', function () {
  headerElement.innerHTML = 'New Header!!!';
});
