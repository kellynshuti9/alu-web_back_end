#!/usr/bin/env python3
"""Filtered logger module"""

import logging
import re
from typing import List, Tuple


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate fields in a log message using regex"""
    pattern: str = r'(' + '|'.join(fields) + r')=[^' + separator + r']*'
    return re.sub(pattern, r'\1=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class for sensitive data"""

    REDACTION: str = "***"
    FORMAT: str = "[HOLBERTON] %(name)s %(levelname)s " \
                  "%(asctime)-15s: %(message)s"
    SEPARATOR: str = ";"

    def __init__(self, fields: List[str]) -> None:
        """Initialize formatter with fields to redact"""
        super().__init__(self.FORMAT)
        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format log record and redact sensitive fields"""
        msg: str = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            msg, self.SEPARATOR)
