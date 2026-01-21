#!/usr/bin/env python3
"""User views
"""
from api.v1.views import app_views
from flask import jsonify, request
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users():
    """Retrieve list of users
    """
    users_list = []

    for user in User.all().values():
        users_list.append(user.to_json())

    return jsonify(users_list)
