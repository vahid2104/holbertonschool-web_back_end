#!/usr/bin/env python3
"""Utilities for secure password hashing and verification with bcrypt."""

import bcrypt


def generate_password_hash(raw_password: str) -> bytes:
    """
    Generate and return a bcrypt hash from a plain text password.
    """
    password_bytes = raw_password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt)


def verify_password(stored_hash: bytes, candidate_password: str) -> bool:
    """
    Verify whether the provided password corresponds to the stored hash.
    """
    return bcrypt.checkpw(candidate_password.encode("utf-8"), stored_hash)
