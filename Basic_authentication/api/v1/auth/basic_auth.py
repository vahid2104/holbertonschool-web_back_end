#!/usr/bin/env python3
"""BasicAuth module
"""
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract Base64 part of Basic Authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract user email and password from decoded Base64
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        email, pwd = decoded_base64_authorization_header.split(":", 1)
        return (email, pwd)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Return User instance based on email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        from models.user import User

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        if users is None or len(users) == 0:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Overload current_user to retrieve user from request
        """
        auth_header = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(auth_header)
        decoded = self.decode_base64_authorization_header(b64)
        email, pwd = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(email, pwd)
