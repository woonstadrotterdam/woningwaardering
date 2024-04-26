from decimal import BasicContext, setcontext
import os
import sys
import time
from types import TracebackType
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
    logger.debug(f"Tijdzone ingesteld via environment variable: {timezone}")


def handle_unhandled_exception(
    exception_type: type[BaseException],
    exception_value: BaseException,
    exception_traceback: TracebackType | None,
) -> None:
    if issubclass(exception_type, KeyboardInterrupt):
        return
    logger.exception(exception_value)
    sys.__excepthook__(exception_type, exception_value, exception_traceback)
    return


sys.excepthook = handle_unhandled_exception
