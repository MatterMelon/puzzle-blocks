from loguru import logger

from .loggger_domain import LoggerDomain


def get_logger(domain: LoggerDomain):
    return logger.bind(domain=domain)