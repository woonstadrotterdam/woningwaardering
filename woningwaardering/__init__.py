from decimal import BasicContext, setcontext
import os
import time
from loguru import logger


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
