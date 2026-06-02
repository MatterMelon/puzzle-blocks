from loguru import logger

from config.levels_config import LEVELS_CONFIG

from ..tilemap import Tilemap

_TILEMAP_REGISTRY: dict[str, type[Tilemap]] = {}

def register_tilemap(cls: type[Tilemap]) -> type[Tilemap]:
    suffix = LEVELS_CONFIG.TILEMAP_SUFFIX

    if not cls.__name__.endswith(suffix):
        raise AttributeError("Tilemap: {class_name} needs to end with {suffix}", class_name=cls.__name__, suffix=suffix)

    tilemap_id = cls.__name__.split(suffix)[0].lower()
    _TILEMAP_REGISTRY[tilemap_id] = cls
    logger.success("Tilemap: '{id}' registered", id=tilemap_id)
    
    return cls