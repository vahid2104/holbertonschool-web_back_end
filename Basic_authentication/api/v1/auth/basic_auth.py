#!/usr/bin/env python3
"""Basic authentication module
"""
import base64
from typing import List, Tuple, TypeVar

from api.v1.auth.auth import Auth
from models.user import User as UserModel

User = TypeVar('User')


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract Base64 part of Authorization header for Basic Auth
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """Extract user email and password from decoded Base64 string
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        email, pwd = decoded_base64_authorization_header.split(':', 1)
        return (email, pwd)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> User:
        """Retrieve User instance based on email and password
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None

        try:
            users = UserModel.search({'email': user_email})
        except Exception:
            return None

        if users is None or len(users) == 0:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> User:
        """Retrieve User instance for a request using Basic Auth
        """
        auth_header = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(auth_header)
        decoded = self.decode_base64_authorization_header(b64)
        user_email, user_pwd = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(user_email, user_pwd)
