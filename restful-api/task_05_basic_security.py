from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_ACCESS_CSRF_DISABLED'] = True

jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify user credentials for HTTP Basic Authentication.

    Args:
        username (str): The username to verify
        password (str): The plain text password to verify

    Returns:
        str or None: Returns username if credentials are valid, None otherwise
    """
    if username in users and check_password_hash(
        users[username]["password"], password
    ):
        return username


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Protected endpoint requiring HTTP Basic Authentication.

    Returns:
        tuple: JSON response with success message and HTTP status code 200
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate user and generate JWT access token.

    Expects JSON payload with 'username' and 'password' fields.

    Returns:
        tuple: JSON response containing access token or error message
               with appropriate HTTP status code (200, 400, or 401)
    """
    try:
        data = request.get_json(force=True)
        if data is None:
            return jsonify({"error": "Invalid JSON"}), 400
        username = data.get("username", '')
        password = data.get("password", '')
    except (ValueError, TypeError, UnicodeDecodeError):
        return jsonify({"error": "Invalid JSON"}), 400

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if verify_password(username, password):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Protected endpoint requiring valid JWT token.

    Returns:
        str: Success message confirming JWT authentication
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin_only():
    """
    Admin-only protected endpoint requiring JWT token and admin role.

    Verifies that the authenticated user has admin privileges.

    Returns:
        tuple or str: JSON error response with status code 403 if user
                     is not admin, or success message if user has admin access
    """
    username = get_jwt_identity()
    user = users.get(username)
    if not user or user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle unauthorized JWT access attempts.

    Args:
        err: The authorization error object

    Returns:
        tuple: JSON error response with status code 401
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid JWT token errors.

    Args:
        err: The invalid token error object

    Returns:
        tuple: JSON error response with status code 401
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired JWT token errors.

    Args:
        err: The expired token error object

    Returns:
        tuple: JSON error response with status code 401
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked JWT token errors.

    Args:
        err: The revoked token error object

    Returns:
        tuple: JSON error response with status code 401
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle cases where a fresh JWT token is required.

    Args:
        err: The fresh token required error object

    Returns:
        tuple: JSON error response with status code 401
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
