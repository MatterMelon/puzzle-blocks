from pygame import Surface

from core.logging.logger import LoggerDomain, get_logger
from world.tilemap.exceptions import TilemapError
from world.tilemap.tilemap_renderer import TilemapRenderer

from .exceptions import LevelError
from .level_data import LevelData

logger = get_logger(LoggerDomain.LEVEL)

class Level:
    def __init__(self, data: LevelData):
        super().__init__()
        if data is None:
            raise ValueError("Level: Cannot build a level with None data")
        # TODO: Разпределить данные из data по полям класса: id, description, goals...
        self._data = data
        self._tilemap_renderer: TilemapRenderer = TilemapRenderer(data.map_data.tilemap_layers)

    def build(self) -> None:
        logger.info(f"Start building '{self._data.id}'")
        try:
            self._tilemap_renderer.build()
        except(TilemapError):
            logger.exception(f"Error occured on building a tilemap for '{self._data.id}' ")
            raise LevelError()
        logger.success(f"'{self._data.id}' built successfully")

    def draw(self, surface: Surface) -> None:
        self._tilemap_renderer.render(surface)

    def update(self, dt: float) -> None:
        pass