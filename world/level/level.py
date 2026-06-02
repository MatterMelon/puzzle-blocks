from loguru import logger
from pygame import Surface

from world.tilemap.exceptions import TilemapError
from world.tilemap.tilemap_renderer import TilemapRenderer

from .exceptions import LevelError
from .level_data import LevelData


class Level:
    def __init__(self, data: LevelData):
        if data is None:
            raise ValueError("Level: Cannot build a level with None data")
        # TODO: Разпределить данные из data по полям класса: id, description, goals...
        self._data = data
        self._tilemap_renderer: TilemapRenderer = TilemapRenderer(data.map_data.tilemap_layers)

    def build(self) -> None:
        logger.info(f"Level: Start building '{self._data.id}'")
        try:
            self._tilemap_renderer.build()
        except(TilemapError):
            logger.exception(f"Level: Error occured on building a tilemap for '{self._data.id}' ")
            raise LevelError()
        logger.success(f"Level: '{self._data.id}' built successfully")

    def draw(self, surface: Surface) -> None:
        self._tilemap_renderer.render(surface)

    def update(self, dt: float) -> None:
        pass