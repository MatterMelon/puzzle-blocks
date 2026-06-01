import json

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
                    data['map'],
                    data['entities']
                )
                logger.success("Level '{id}': Data loaded", id=level_data.id)
                return level_data
        except json.JSONDecodeError:
            logger.exception("Level: Data parsing error")
            # raise LevelLoadError