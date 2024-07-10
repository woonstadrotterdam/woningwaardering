from decimal import BasicContext, setcontext
import os
import sys
import time
from types import TracebackType
from typing import Literal
from loguru import logger
from pydantic import BaseModel


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
    logger.info(f'Tijdzone ingesteld via environment variable "TZ": {timezone}')


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


class CriticalWarningException(Exception):
    pass


class LoggerConfig(BaseModel):
    level: Literal["DEBUG", "INFO", "WARNING"] = "INFO"
    warning_critical: bool = False


def configureer_logger(config: LoggerConfig = LoggerConfig()) -> None:
    # remove bestaande logger
    logger.remove()

    logger.add(sys.stderr, level=config.level)

    # Zet een handler die WarningCriticalException raised bij een warning
    if config.warning_critical:

        def critical_handler(message):
            # try:
            raise CriticalWarningException(
                f"CriticalWarningException: {message.record['message']}"
            )
            # except

        logger.add(critical_handler, level="WARNING", catch=False)


logger.enable("woningwaardering")
configureer_logger(LoggerConfig(level="INFO", warning_critical=False))

__all__ = ["configureer_logger", "LoggerConfig", "CriticalWarningException", "logger"]
