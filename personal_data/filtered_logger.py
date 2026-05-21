#!/usr/bin/env python3
"""Personal data logging and database module"""

import re
import os
import logging
import mysql.connector
from typing import List, Tuple


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
) -> str:
    """Obfuscate specified fields in a log message"""
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(
        pattern,
        lambda m: f"{m.group(1)}={redaction}",
        message
    )


class RedactingFormatter(logging.Formatter):
    """Redacting formatter that hides sensitive information"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Tuple[str, ...]) -> None:
        """Initialize formatter with fields to redact"""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Redact sensitive fields from log record"""
        return filter_datum(
            self.fields,
            self.REDACTION,
            super().format(record),
            self.SEPARATOR
        )


PII_FIELDS: Tuple[str, ...] = (
    "name",
    "email",
    "phone",
    "ssn",
    "password"
)


def get_logger() -> logging.Logger:
    """Create and return a secure logger for user data"""
    logger: logging.Logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.handlers = []
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Return MySQL database connection using environment variables"""
    return mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )
