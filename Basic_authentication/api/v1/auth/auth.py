#!/usr/bin/env python3
"""Auth module
"""
from typing import List, TypeVar

from flask import request


class Auth:
    """Template class for authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns True if path requires authentication"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Returns the Authorization header value"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user (not implemented)"""
        return None
