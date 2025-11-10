// Récupère la liste de films via l'API SWAPI et ajoute chaque titre dans #list_movies.
const ListMovie = document.querySelector('#list_movies');
const apiURL = 'https://swapi-api.hbtn.io/api/films/?format=json';
fetch(apiURL)
  .then(responce => {
    return responce.json();
  })
  .then(data => {
    const movies = data.results;
    movies.forEach(movie => {
      const li = document.createElement('li');
      const movieTitle = movie.title;
      li.textContent = movieTitle;
      ListMovie.appendChild(li);
    });
  });
