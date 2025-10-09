import csv
# Module : requêtes vers l'API et écriture des résultats en CSV
import requests


def fetch_and_print_posts():
    # Effectue une requête GET vers l'API de test
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    # Affiche le code de réponse pour le débogage
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        for i in data:
            # Affiche le titre de chaque post
            print(i['title'])


def fetch_and_save_posts():
    # Effectue une requête GET et enregistre le résultat en CSV
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        header = ['id', 'title', 'body']

        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)
            # Écrit chaque enregistrement de post dans le CSV
            for post in response.json():
                csv_writer.writerow([
                    post.get('id'),
                    post.get('title'),
                    post.get('body'),
                ])
