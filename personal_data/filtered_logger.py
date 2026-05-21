#!/usr/bin/env python3
"""Filtered logger module"""

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate sensitive fields in a log message"""
    pattern = r'(' + '|'.join(fields) + r')=[^' + separator + r']*'
    return re.sub(pattern, r'\1=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """Redacting formatter that filters sensitive information"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize formatter with fields to redact"""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Return formatted and redacted log message"""
        return filter_datum(
            self.fields,
            self.REDACTION,
            super().format(record),
            self.SEPARATOR
        )
