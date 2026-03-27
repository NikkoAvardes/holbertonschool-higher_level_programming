# SQL – Introduction

Scripts SQL pour découvrir les bases de MySQL : bases, tables et requêtes simples.

## Fichiers

- 0-list_databases.sql – liste toutes les bases de données.
- 1-create_database_if_missing.sql – crée une base de données si elle n’existe pas.
- 2-remove_database.sql – supprime une base de données.
- 3-list_tables.sql – liste les tables d’une base.
- 4-first_table.sql – crée une première table.
- 5-full_table.sql – affiche la structure complète d’une table.
- 6-list_values.sql – affiche toutes les lignes d’une table.
- 7-insert_value.sql – insère une nouvelle ligne.
- 8-count_89.sql – compte les lignes correspondant à une condition.
- 9-full_creation.sql – crée et remplit une table.
- 10-top_score.sql – affiche les scores triés par ordre décroissant.
- 11-best_score.sql – affiche les meilleures entrées selon le score.
- 12-no_cheating.sql – met à jour une ligne sans utiliser SELECT.
- 13-change_class.sql – supprime des entrées selon une condition.
- 14-average.sql – calcule une moyenne sur une colonne.
- 15-groups.sql – regroupe les lignes et agrège les valeurs.
- 16-no_link.sql – sélectionne les lignes avec une valeur non nulle / non vide.

- **Colonnes** : `snake_case` (ex: `user_name`)

### 🔐 Bonnes pratiques

- ✅ Toujours utiliser `IF NOT EXISTS` pour les créations
- ✅ Spécifier les types de données appropriés
- ✅ Utiliser des contraintes (`NOT NULL`, `PRIMARY KEY`)
- ✅ Commenter les requêtes complexes
- ✅ Sauvegarder avant les opérations destructives

### 🐛 Débogage courant

| Erreur                   | Solution                             |
| ------------------------ | ------------------------------------ |
| `Access denied`          | Vérifier les permissions utilisateur |
| `Database doesn't exist` | Créer la base de données d'abord     |
| `Table doesn't exist`    | Vérifier le nom et l'existence       |
| `Syntax error`           | Vérifier la syntaxe SQL              |

---

## 🔗 Ressources

### 📚 Documentation

- [MySQL Official Documentation](https://dev.mysql.com/doc/)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)

### 🛠️ Outils utiles

- **MySQL Workbench** - Interface graphique
- **phpMyAdmin** - Administration web
- **DBeaver** - Client universel
- **Sequel Pro** - Client macOS

### 📖 Lectures complémentaires

- [Database Design Basics](https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL Best Practices](https://dev.mysql.com/doc/mysql-tutorial-excerpt/8.0/en/)

---

<div align="center">

**🎓 Projet réalisé dans le cadre de la formation Holberton School**

_Maîtrisez les bases de données relationnelles avec MySQL_

[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red)](https://github.com/NikkoAvardes)
[![SQL](https://img.shields.io/badge/Language-SQL-blue)](https://www.mysql.com/)

</div>
