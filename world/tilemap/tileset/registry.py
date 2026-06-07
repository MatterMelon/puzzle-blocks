from config.levels_config import LEVELS_CONFIG
from core.logging.logger import LoggerDomain, get_logger
from .tileset import Tileset

from ..tilemap import Tilemap

_TILEMAP_REGISTRY: dict[str, type[Tileset]] = {}

logger = get_logger(LoggerDomain.TILEMAP)

def register_tileset(cls: type[Tileset]) -> type[Tileset]:
    suffix = LEVELS_CONFIG.TILESET_SUFFIX

    if not cls.__name__.endswith(suffix):
        raise AttributeError(f"{cls.__name__} needs to end with {suffix}")

    tilemap_id = cls.__name__.split(suffix)[0].lower()
    _TILEMAP_REGISTRY[tilemap_id] = cls
    logger.success(f"'{tilemap_id}' registered")
    
    return cls