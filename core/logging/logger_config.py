import sys

from loguru import logger

LOG_FORMAT = (
    "<green>{time:HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{extra[domain]: <12}</cyan> | "
    "<magenta>{name}:{line}</magenta> | "
    "<level>{message}</level>"
)

def configure_logging():
    logger.remove()
    logger.configure(extra={"domain": "GLOBAL"})
    logger.add(
        sys.stderr,
        format=LOG_FORMAT,
        colorize=True,
        backtrace=True,
        diagnose=False,
    )