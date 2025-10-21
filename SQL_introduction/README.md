# 🗄️ SQL Introduction

<div align="center">

![SQL](https://img.shields.io/badge/SQL-MySQL-blue?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Learning-brightgreen?style=for-the-badge)
![Progress](https://img.shields.io/badge/Progress-100%25-success?style=for-the-badge)

**Introduction aux bases de données relationnelles et au langage SQL**

*Apprenez les fondamentaux de SQL avec MySQL*

</div>

---

## 📋 Table des Matières

- [📖 Description](#-description)
- [🎯 Objectifs d'apprentissage](#-objectifs-dapprentissage)
- [📂 Structure du projet](#-structure-du-projet)
- [🚀 Installation et configuration](#-installation-et-configuration)
- [📚 Liste des exercices](#-liste-des-exercices)
- [💡 Exemples d'utilisation](#-exemples-dutilisation)
- [📝 Notes importantes](#-notes-importantes)
- [🔗 Ressources](#-ressources)

---

## 📖 Description

Ce projet constitue une introduction complète au **SQL (Structured Query Language)** et aux bases de données relationnelles. Vous apprendrez à manipuler des données en utilisant MySQL, depuis les opérations de base jusqu'aux requêtes plus complexes.

### 🎓 Compétences développées

- ✅ Création et gestion de bases de données
- ✅ Manipulation de tables (CREATE, DROP, ALTER)
- ✅ Insertion, mise à jour et suppression de données
- ✅ Requêtes de sélection avec filtres et tri
- ✅ Fonctions d'agrégation (COUNT, AVG, SUM)
- ✅ Regroupement et tri des résultats

---

## 🎯 Objectifs d'apprentissage

À la fin de ce projet, vous serez capable de :

- **Comprendre** ce qu'est une base de données relationnelle
- **Expliquer** ce que signifie SQL et MySQL
- **Créer** une base de données dans MySQL
- **Différencier** DDL et DML
- **Créer ou modifier** une table
- **Sélectionner** des données depuis une table
- **Insérer, mettre à jour ou supprimer** des données
- **Utiliser** les sous-requêtes
- **Utiliser** les fonctions MySQL

---

## 📂 Structure du projet

```
SQL_introduction/
├── 📄 README.md                      # Ce fichier
├── 🔍 0-list_databases.sql           # Lister toutes les bases de données
├── 🏗️ 1-create_database_if_missing.sql # Créer une base de données
├── 🗑️ 2-remove_database.sql         # Supprimer une base de données
├── 📋 3-list_tables.sql              # Lister les tables
├── 🏗️ 4-first_table.sql             # Créer une première table
├── 📊 5-full_table.sql               # Description complète d'une table
├── 👀 6-list_values.sql              # Afficher toutes les lignes
├── ➕ 7-insert_value.sql             # Insérer une nouvelle ligne
├── 🔢 8-count_89.sql                 # Compter les enregistrements
├── 🏗️ 9-full_creation.sql           # Créer et peupler une table
├── 🏆 10-top_score.sql               # Trier par score (décroissant)
├── 🌟 11-best_score.sql              # Filtrer les meilleurs scores
├── 🚫 12-no_cheating.sql             # Mettre à jour sans SELECT
├── 🔄 13-change_class.sql            # Supprimer les scores faibles
├── 📊 14-average.sql                 # Calculer la moyenne
├── 👥 15-groups.sql                  # Regrouper par score
└── 🔗 16-no_link.sql                 # Exclure les entrées sans nom
```

---

## 🚀 Installation et configuration

### Prérequis

- **MySQL Server** (version 8.0 ou supérieure)
- **MySQL Client** pour exécuter les scripts
- Accès en ligne de commande

### Installation sur Ubuntu/Debian

```bash
# Mettre à jour les paquets
sudo apt update

# Installer MySQL Server
sudo apt install mysql-server

# Sécuriser l'installation
sudo mysql_secure_installation

# Se connecter à MySQL
sudo mysql -u root -p
```

### Installation sur macOS

```bash
# Avec Homebrew
brew install mysql

# Démarrer le service
brew services start mysql

# Se connecter
mysql -u root -p
```

---

## 📚 Liste des exercices

| Fichier | Description | Concepts clés |
|---------|-------------|---------------|
| `0-list_databases.sql` | 📋 Afficher toutes les bases de données | `SHOW DATABASES` |
| `1-create_database_if_missing.sql` | 🏗️ Créer une base de données | `CREATE DATABASE` |
| `2-remove_database.sql` | 🗑️ Supprimer une base de données | `DROP DATABASE` |
| `3-list_tables.sql` | 📊 Lister les tables | `SHOW TABLES` |
| `4-first_table.sql` | 🏗️ Créer une table | `CREATE TABLE` |
| `5-full_table.sql` | 📋 Décrire une table | `SHOW CREATE TABLE` |
| `6-list_values.sql` | 👀 Afficher les données | `SELECT *` |
| `7-insert_value.sql` | ➕ Insérer des données | `INSERT INTO` |
| `8-count_89.sql` | 🔢 Compter avec condition | `COUNT()`, `WHERE` |
| `9-full_creation.sql` | 🏗️ Créer et peupler | `CREATE`, `INSERT` |
| `10-top_score.sql` | 🏆 Trier par score | `ORDER BY DESC` |
| `11-best_score.sql` | 🌟 Filtrer les scores élevés | `WHERE`, `ORDER BY` |
| `12-no_cheating.sql` | 🚫 Mise à jour directe | `UPDATE` |
| `13-change_class.sql` | 🔄 Suppression conditionnelle | `DELETE WHERE` |
| `14-average.sql` | 📊 Calculer la moyenne | `AVG()` |
| `15-groups.sql` | 👥 Regrouper les données | `GROUP BY` |
| `16-no_link.sql` | 🔗 Exclure valeurs nulles | `WHERE NOT NULL` |

---

## 💡 Exemples d'utilisation

### Exécution d'un script SQL

```bash
# Se connecter à MySQL et exécuter un script
mysql -u root -p < 0-list_databases.sql

# Ou depuis MySQL
mysql> USE hbtn_0c_0;
mysql> source 4-first_table.sql;
```

### Exemple de requête

```sql
-- Créer une base de données
CREATE DATABASE IF NOT EXISTS school_db;

-- Utiliser la base de données
USE school_db;

-- Créer une table étudiants
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    grade DECIMAL(3,2)
);

-- Insérer des données
INSERT INTO students (name, age, grade) VALUES
('Alice', 20, 85.5),
('Bob', 22, 92.0),
('Charlie', 19, 78.5);

-- Sélectionner les meilleurs étudiants
SELECT name, grade
FROM students
WHERE grade >= 80
ORDER BY grade DESC;
```

---

## 📝 Notes importantes

### ⚠️ Conventions de nommage

- **Bases de données** : `snake_case` (ex: `hbtn_0c_0`)
- **Tables** : `snake_case` (ex: `first_table`)
- **Colonnes** : `snake_case` (ex: `user_name`)

### 🔐 Bonnes pratiques

- ✅ Toujours utiliser `IF NOT EXISTS` pour les créations
- ✅ Spécifier les types de données appropriés
- ✅ Utiliser des contraintes (`NOT NULL`, `PRIMARY KEY`)
- ✅ Commenter les requêtes complexes
- ✅ Sauvegarder avant les opérations destructives

### 🐛 Débogage courant

| Erreur | Solution |
|--------|----------|
| `Access denied` | Vérifier les permissions utilisateur |
| `Database doesn't exist` | Créer la base de données d'abord |
| `Table doesn't exist` | Vérifier le nom et l'existence |
| `Syntax error` | Vérifier la syntaxe SQL |

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

*Maîtrisez les bases de données relationnelles avec MySQL*

[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-red)](https://github.com/NikkoAvardes)
[![SQL](https://img.shields.io/badge/Language-SQL-blue)](https://www.mysql.com/)

</div>
