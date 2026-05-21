#!/usr/bin/env python3
"""Filtered logger module"""

import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscates sensitive fields using regex"""
    return re.sub(rf"({'|'.join(fields)})=[^{separator}]*", r"\1=" + redaction, message)
