// Récupère via fetch le nom d'un personnage SWAPI et l'insère dans #character.
const TagCharacter = document.querySelector('#character');
const Url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
fetch(Url)
  .then(responce => {
    return responce.json();
  })
  .then(data => {
    const TaskName = data.name;
    TagCharacter.innerHTML = TaskName;
  });
