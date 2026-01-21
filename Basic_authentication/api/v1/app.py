#!/usr/bin/env python3
"""Main Flask app
"""
import os

from flask import Flask, jsonify, abort, request
from flask_cors import CORS

from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None

AUTH_TYPE = os.getenv('AUTH_TYPE')
if AUTH_TYPE == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif AUTH_TYPE == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.errorhandler(401)
def unauthorized(error) -> str:
    """401 error handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """403 error handler"""
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """Filter each request"""
    if auth is None:
        return

    excluded = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    user = auth.current_user(request)
    if user is None:
        abort(403)

    request.current_user = user


if __name__ == "__main__":
    host = os.getenv('API_HOST', '0.0.0.0')
    port = int(os.getenv('API_PORT', '5000'))
    app.run(host=host, port=port)
