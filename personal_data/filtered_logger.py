#!/usr/bin/env python3
"""Filtered logger module"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscate sensitive fields in a log message"""
    pattern = r"(" + "|".join(fields) + r")=[^" + separator + r"]*"
    return re.sub(pattern, r"\1=" + redaction, message)
