import json

from level.level_map_data import LevelMapData
from loguru import logger

from .level_data import LevelData
from .level_loader import LevelLoader


class JsonLevelLoader(LevelLoader):
    @staticmethod
    def load(path: str) -> LevelData:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                level_data = LevelData(
                    str.strip(data['id']),
                    str.strip(data['name']),
                    str.strip(data['description']),
                    data['goals'],
                    LevelMapData(
                        data['map']['width'],
                        data['map']['height'],
                        data['map']['tiles'],
                    ),
                    data['entities']
                )
                logger.success("Level: '{id}' data loaded", id=level_data.id)
                return level_data
        except json.JSONDecodeError:
            logger.exception("Level: Data parsing error")
            # raise LevelLoadError