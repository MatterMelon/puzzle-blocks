from loguru import logger
from loguru._logger import Logger

from core.logging.loggger_domain import LoggerDomain


def get_logger(domain: LoggerDomain) -> Logger:
    return logger.bind(domain=domain)