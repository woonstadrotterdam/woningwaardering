from decimal import BasicContext, setcontext
import os
import sys
import time
from types import TracebackType
from typing import TextIO
import warnings
from loguru import logger

logger.disable("woningwaardering")

# Set context for all calculations to avoid rounding errors
# See https://docs.python.org/3/library/decimal.html#rounding
setcontext(BasicContext)


default_timezone = "Europe/Amsterdam"

timezone = os.environ.get("TZ")

if timezone is None:
    logger.info('Geen environment variable "TZ" gevonden')
    logger.info(f"Tijdzone wordt ingesteld op {default_timezone}")
    os.environ["TZ"] = default_timezone
    time.tzset()
else:
    logger.debug(f'Tijdzone ingesteld via environment variable "TZ": {timezone}')


def handle_unhandled_exception(
    exception_type: type[BaseException],
    exception_value: BaseException,
    exception_traceback: TracebackType | None,
) -> None:
    """
    Deze functie zorgt ervoor dat onverwachte uitzonderingen gelogged worden
    en negeert daarbij uitzonderingen die ontstaan zijn door een KeyboardInterrupt.
    Als de uitzondering van het type `KeyboardInterrupt` is, wordt de uitvoering
    onderbroken zonder enige verdere actie.
    Een voorbeeld van een `KeyboardInterrupt` is wanneer een gebruiker op Ctrl+C drukt.
    """
    if issubclass(exception_type, KeyboardInterrupt):
        return
    logger.exception(exception_value)
    sys.__excepthook__(exception_type, exception_value, exception_traceback)
    return


sys.excepthook = handle_unhandled_exception


# Zet de warning filter zodat UserWarnings een error worden
warnings.simplefilter("error", UserWarning)


def warning_handler(
    message: Warning | str,
    category: type[Warning],
    filename: str,
    lineno: int,
    file: TextIO | None = None,
    line: str | None = None,
) -> None:
    """
    Deze functie logt en print warning messages.

    Args:
        message (Warning | str): De warning message.
        category (type[Warning]): De warning categorie.
        filename (str): De naam van het bestand waar de warning is gedaan.
        lineno (int): Het regelnummer waarop de warning is gedaan.
        file (TextIO | None, optional): Het bestand waar de warning is gedaan. Default None.
        line (str | None, optional): De regel code waar de waaring is gedaan. Default None.
    """
    warning_message = f"{category.__name__}: {message}"
    try:
        logger.opt(depth=2, exception=None).warning(warning_message)
    except TypeError:
        # Fallback if logger.warning de message niet kan loggen
        print(f"{filename}:{lineno} - {category.__name__}: {message} - {file}:{line}")
    finally:
        # Print warning in sys.stderr
        print(f"{filename}:{lineno} - {warning_message}", file=sys.stderr)


warnings.showwarning = warning_handler

__all__ = ["set_warning_filter"]
