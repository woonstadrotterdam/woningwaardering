import sys

from loguru import logger


def verkort_path(name, regel):
    name = name.replace("zelfstandige_woonruimten", "zelf")
    parts = name.split(".")
    if len(parts) > 4:
        package = parts[0]
        stelsel = parts[-3]
        stelselgroep = parts[-1]
        path = f"{package}.{stelsel}.{stelselgroep}"
    else:
        path = name
    return f"{path}:{regel}"


def custom_filter(record):
    record["extra"]["formatted_name_with_line"] = verkort_path(
        record["name"], record["line"]
    )
    return True


logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{extra[formatted_name_with_line]}</cyan> | <blue>{message}</blue>",
    level="DEBUG",
    filter=custom_filter,
)
