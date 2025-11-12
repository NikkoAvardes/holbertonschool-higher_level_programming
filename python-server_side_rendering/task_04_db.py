#!/usr/bin/python3
"""Flask application with dynamic content using loops and conditions."""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def create_database():
    """Create and populate SQLite database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def home():
    """Home page route."""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page route."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Contact page route."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Items page route."""
    with open('items.json', 'r') as f:
        data = json.load(f)
        items_list = data.get('items', [])
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products_list = []

    if source == 'json':
        try:
            with open('products.json') as json_file:
                products_list = json.load(json_file)
        except FileNotFoundError:
            return render_template('product_display.html',
                                   error="JSON file not found")
    elif source == 'csv':
        try:
            with open('products.csv') as csv_file:
                reader = csv.DictReader(csv_file)
                products_list = []
                for row in reader:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products_list.append(row)
        except FileNotFoundError:
            return render_template('product_display.html',
                                   error="CSV file not found")
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
            products_list = []
            for row in rows:
                products_list.append({
                    'id': row[0],
                    'name': row[1],
                    'category': row[2],
                    'price': row[3]
                })
            conn.close()
        except Exception:
            return render_template('product_display.html',
                                   error="Database error")
    else:
        return render_template('product_display.html',
                               error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            products_list = [
                product for product in products_list if product['id']
                == product_id]
            if not products_list:
                return render_template(
                    'product_display.html',
                    error="Product not found")
        except ValueError:
            return render_template('product_display.html',
                                   error="Invalid product ID")
    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
