#!/usr/bin/env python3
"""Utilities for redacting sensitive fields from log messages."""

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
