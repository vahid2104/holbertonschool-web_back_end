#!/usr/bin/env python3
"""Auth module for authentication handling"""
from typing import List, TypeVar
from flask import request


User = TypeVar('User')


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path

        Args:
            path (str): The request path
            excluded_paths (List[str]): List of paths that do not require auth

        Returns:
            bool: True if auth is required, False otherwise
        """
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
        """
        Returns the Authorization header from the request

        Args:
            request: Flask request object

        Returns:
            str: Authorization header value
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """
        Returns the current authenticated user

        Args:
            request: Flask request object

        Returns:
            User: The current user
        """
        return None
