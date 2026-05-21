#!/usr/bin/env python3
"""Password encryption module"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password using bcrypt and return a salted hash"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
