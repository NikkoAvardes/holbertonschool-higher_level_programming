# Python – Object-relational mapping

Scripts qui relient des objets Python à une base de données MySQL en utilisant MySQLdb et SQLAlchemy.

## Fichiers principaux

- 0-select_states.py – liste tous les États depuis la base `hbtn_0e_0_usa` (MySQLdb).
- 1-filter_states.py – affiche les États dont le nom commence par « N ».
- 2-my_filter_states.py – filtre les États par nom (version vulnérable à l’injection SQL).
- 3-my_safe_filter_states.py – filtre les États par nom de manière sécurisée (requêtes paramétrées).
- 4-cities_by_state.py – affiche les villes associées à chaque État.
- 5-filter_cities.py – affiche les villes d’un État donné.
- 6-model_state.py – définit la classe `State` avec SQLAlchemy.
- 7-model_state_fetch_all.py – récupère tous les objets `State` avec SQLAlchemy.
- 8-model_state_fetch_first.py – récupère le premier objet `State`.
- 9-model_state_filter_a.py – récupère les États contenant la lettre « a ».
- 10-model_state_my_get.py – récupère un `State` par identifiant.
- 11-model_state_insert.py – insère un nouvel objet `State`.
- 12-model_state_update_id_2.py – met à jour le `State` dont l’id est 2.
- 13-model_state_delete_a.py – supprime les `State` contenant la lettre « a ».
- 14-model_city_fetch_by_state.py – affiche les villes avec leur État en utilisant les modèles SQLAlchemy.

Les fichiers \*.sql contiennent les scripts SQL de création des tables ; `model_state.py` et `model_city.py` définissent les classes mappées.
