
"""Simple Flask API with in-memory users storage.

Minimal example for learning and local testing.
"""

from flask import Flask, jsonify, request


app = Flask(__name__)

# In-memory users store (example only, not persistent)
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
# Root endpoint: simple HTML welcome message.
def home():
    return "<p>Welcome to the Flask API!</p>"


@app.route("/data")
def list_users():
    # Return list of usernames as JSON.
    return jsonify(list(users.values()))


@app.route('/status')
def status():
    # Health-check endpoint.
    return 'OK'


@app.route('/user/<username>')
def get_users(username):
    # Return user data for given username or 404.
    if username in users:
        return jsonify(users[username]), 200
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    # Add a new user from JSON payload.
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data.get("username")

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    # Run the Flask development server.
    app.run()
