#!/usr/bin/python3
"""Flask application with dynamic content using loops and conditions."""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


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
