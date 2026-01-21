#!/usr/bin/env python3
"""Auth module"""
from typing import List, TypeVar
from flask import request


User = TypeVar('User')


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if path requires auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """Returns the Authorization header value"""
        return None

    def current_user(self, request=None) -> User:
        """Returns the current user"""
        return None
