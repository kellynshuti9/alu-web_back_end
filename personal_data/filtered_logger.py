#!/usr/bin/env python3
"""Filtered logger module"""

import logging
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscate sensitive fields in a log message"""
    return re.sub(r'(' + '|'.join(fields) + r')=[^' + separator + r']*',
                  r'\1=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(
            self.fields,
            self.REDACTION,
            super().format(record),
            self.SEPARATOR
        )
