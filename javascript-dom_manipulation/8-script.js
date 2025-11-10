// Au chargement du DOM, récupère une salutation et l'insère dans #hello.
// Montre l'utilisation de DOMContentLoaded + fetch + insertion de texte.
document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const idHello = document.querySelector('#hello');
  if (idHello) {
    fetch(url)
      .then(responce => {
        return responce.json();
      })
      .then(data => {
        idHello.textContent = data.hello;
      });
	  
  }
});
