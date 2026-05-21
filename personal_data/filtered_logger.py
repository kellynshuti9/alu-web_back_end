#!/usr/bin/env python3
"""Filtered logger module"""

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate sensitive fields in log messages"""
    return re.sub(r'(' + '|'.join(fields) + r')=[^' + separator + r']*',
                  r'\1=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """Redacting formatter that filters sensitive info"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(
            self.fields,
            self.REDACTION,
            super().format(record),
            self.SEPARATOR
        )
