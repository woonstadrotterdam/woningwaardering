import sys
import warnings
from typing import Any, TextIO

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
    logger.warning(f"{UserWarning.__name__}: {message}")
    _original_showwarning(message, category, filename, lineno, file, line)


def verkort_path(name: str, regel: int, dev: bool = False) -> str:
    name = name.replace("zelfstandige_woonruimten", "zelfstandig")
    parts = name.split(".")
    if len(parts) > 4:
        package = parts[0]
        stelsel = parts[-3]
        stelselgroep = parts[-1]
        path = f"{package}.{stelsel}.{stelselgroep}"
    else:
        path = name
    if dev:
        path = path.replace("woningwaardering.", "")
    return f"{path}:{regel}"


def custom_filter(record: dict[str, Any]) -> bool:
    record["extra"]["formatted_name_with_line"] = verkort_path(
        record["name"], record["line"]
    )
    return True


format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <7}</level> | <cyan>{extra[formatted_name_with_line]}</cyan> | <level>{message}</level>"
logger.remove()
logger.add(
    sys.stderr,
    format=format,
    level="DEBUG",
    filter=custom_filter,
)
