// Bascule les classes 'red' / 'green' du header au clic — montre le toggle via classes.
const headerElement = document.querySelector('header');
const idButton = document.querySelector('#toggle_header');
if (headerElement && idButton) {
  idButton.addEventListener('click', function () {
    // Si le header a 'red', on passe à 'green', sinon inversement.
    if (headerElement.classList.contains('red')) {
      headerElement.classList.remove('red');
      headerElement.classList.add('green');
    } else {
      headerElement.classList.remove('green');
      headerElement.classList.add('red');
    }
  });
}
