#!/usr/bin/env python3
"""Basic authentication module"""

import base64
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User as UserModel

User = TypeVar('User')


class BasicAuth(Auth):
    """Basic authentication class"""

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header from the request
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 authorization header
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
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Extracts user email and password from decoded Base64 value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return decoded_base64_authorization_header.split(':', 1)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> User:
        """
        Returns User instance based on email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = UserModel.search({'email': user_email})
        except Exception:
            return None

        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> User:
        """
        Retrieves the User instance for a request using Basic Auth
        """
        auth_header = self.authorization_header(request)
        base64_part = self.extract_base64_authorization_header(auth_header)
        decoded = self.decode_base64_authorization_header(base64_part)
        email, password = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(email, password)
