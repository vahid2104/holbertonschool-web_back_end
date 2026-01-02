#!/usr/bin/env python3
"""Utilities for redacting sensitive fields from log messages."""

import logging
import re
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """Return a log message with specified fields redacted."""
    pattern = (
        rf"({'|'.join(map(re.escape, fields))})="
        rf"[^{re.escape(separator)}]*"
    )
    return re.sub(pattern, rf"\1={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class."""

    REDACTION = "***"
    FORMAT = (
        "[HOLBERTON] %(name)s %(levelname)s "
        "%(asctime)-15s: %(message)s"
    )
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize formatter with fields to redact."""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the record and redact sensitive fields."""
        message = super().format(record)
        return filter_datum(
            self.fields,
            self.REDACTION,
            message,
            self.SEPARATOR
        )
