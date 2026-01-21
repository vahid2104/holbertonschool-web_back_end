#!/usr/bin/env python3
"""Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Status endpoint"""
    return jsonify({"status": "OK"})


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """Trigger 401"""
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden():
    """Trigger 403"""
    abort(403)
