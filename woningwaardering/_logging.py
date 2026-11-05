from __future__ import annotations

import warnings
from typing import TextIO

from loguru import logger

# om warnings te loggen
_original_showwarning = warnings.showwarning


def log_userwarning(
    message: Warning | str,
    category: type[Warning],
    filename: str,
    lineno: int,
    file: TextIO | None = None,
    line: str | None = None,
) -> None:
    logger.warning(f"{category.__name__}: {message}")
    _original_showwarning(message, category, filename, lineno, file, line)
