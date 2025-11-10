// Ajoute un nouvel élément <li> 'Item' à la liste `.my_list` au clic.
const LiElement = document.querySelector('.my_list');
const idButton = document.querySelector('#add_item');
if (LiElement && idButton) {
  idButton.addEventListener('click', function () {
    const li = document.createElement('li');
    const text = document.createTextNode('Item');
    li.appendChild(text);
    LiElement.appendChild(li);
  });
}
