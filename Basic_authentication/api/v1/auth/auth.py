#!/usr/bin/env python3
"""Auth module
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method to check if path requires auth
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path = path + '/'

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Public method to return authorization header
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method to return current user
        """
        return None
