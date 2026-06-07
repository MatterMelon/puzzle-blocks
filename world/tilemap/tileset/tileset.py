from abc import ABC
from enum import IntEnum

from pygame.sprite import Group

from core.logging.logger import get_logger
from core.logging.loggger_domain import LoggerDomain
from world.spritesheet import SpriteSheet
from world.tilemap.exceptions import MissingTileData
from world.tilemap.tile.tile import Tile
from world.tilemap.tile.tile_definition import TileDefinition

logger = get_logger(LoggerDomain.TILEMAP)

class Tileset(ABC):
    def __init__(self, spritesheet: SpriteSheet, tiles_data: dict[int, TileDefinition]):
        self._spritesheet: SpriteSheet = spritesheet
        self._tiles_data: dict[int, TileDefinition] = tiles_data

    class TileType(IntEnum):
        pass

    def __init_subclass__(cls):
        super().__init_subclass__()

        if not hasattr(cls, 'TileType'):
            raise TypeError(
                f'{cls.__name__} must define TileType'
            )

        if not issubclass(cls.TileType, IntEnum):
            raise TypeError(
                f'{cls.__name__}.TileType must inherit IntEnum'
            )

    def place_tile(self, tile_id: int, pos_x: int, pos_y: int, use_grid_snap: bool = False) -> tuple[Tile, Tile | None]:
        td = self._tiles_data.get(tile_id)
        tile: Tile
        collision: Tile

        if not td:
            raise MissingTileData(f"Tried to get TileData by ID = {tile_id}")

        img = self._spritesheet.get_image(td.frame_x, td.frame_y, td.frame_width, td.frame_height)
        tile = Tile(tile_id, img, td.props)

        if use_grid_snap:
            tile.rect.x = pos_x * self._spritesheet.get_grid_size()
            tile.rect.y = pos_y * self._spritesheet.get_grid_size()
        else:
            tile.rect.x = pos_x
            tile.rect.y = pos_y

        if td.props and td.props.collision:
            return tile, tile
        return tile, None


    def delete_tile(self) -> None:
        pass

    def resolve_tile_id(self, tile_name: str) -> int:
        """
        Получает ID тайла по его строковому имени.
        :param tile_name: Строковое имя тайла для поиска.
        :return: Числовой ID тайла. Если имя не найдено, возвращает ID тайла UNKNOWN.
        """
        try:
            return self.TileType[tile_name]
        except KeyError:
            logger.warning(
                F"Missing tile ID:'{tile_name}' in '{self}' \n"
                "Replacing with 'UNKNOWN'"
            )

            # TODO: Добавить тайлмап для текстуры UNKNOWN.
            #       Сейчас она берется из самого тайлмапа с ошибкой.
            return self.TileType.UNKNOWN