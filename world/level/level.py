from pygame import Surface
from pygame.sprite import RenderUpdates

from core.logging.logger import LoggerDomain, get_logger
from world.tilemap.exceptions import TilemapError
from world.tilemap.tilemap_builder import TilemapBuilder

from .exceptions import LevelError
from .level_data import LevelData

logger = get_logger(LoggerDomain.LEVEL)

class Level:
    def __init__(self, data: LevelData):
        super().__init__()
        if data is None:
            raise ValueError("Cannot build a level with None data")
        self._data = data
        self._tilemap_builder: TilemapBuilder = TilemapBuilder(data.map_data.tilemap_layers)
        self._tilemap: RenderUpdates

    def build(self) -> None:
        logger.info(f"Start building '{self._data.id}'")
        try:
            self._tilemap = self._tilemap_builder.build()
            # self._tilemap_builder.build()
        except(TilemapError):
            logger.exception(f"Error occured on building a tilemap for '{self._data.id}' ")
            raise LevelError()
        logger.success(f"'{self._data.id}' built successfully")

    def draw(self, surface: Surface) -> None:
        self._tilemap.draw(surface)
        # self._tilemap_builder.render(surface)

    def update(self, dt: float) -> None:
        pass