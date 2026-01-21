#!/usr/bin/env python3
"""Auth module"""
from typing import List, TypeVar
from flask import request


User = TypeVar('User')


class Auth:
    """Auth class"""

        def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if path requires authentication"""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False

        return True


    def authorization_header(self, request=None) -> str:
        """Returns the Authorization header value"""
        return None

    def current_user(self, request=None) -> User:
        """Returns the current user"""
        return None
