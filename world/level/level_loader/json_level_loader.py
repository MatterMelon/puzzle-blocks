import json
from abc import abstractmethod

from core.logging.logger import get_logger
from core.logging.loggger_domain import LoggerDomain
from world.level.exceptions import LevelError
from world.level.level_loader.level_loader import LevelLoader
from world.tilemap.tilemap_layer_data import TilemapLayerData

from world.level.level_data import LevelData
from world.level.level_map_data import LevelMapData
from world.entity.entity_data import EntityData

logger = get_logger(LoggerDomain.LEVEL)

class JsonLevelLoader(LevelLoader):
    def __init__(self, file_path: str):
        super().__init__()
        self._path: str = file_path

    def load(self) -> LevelData:
        try:
            with open(self._path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                level_data = LevelData(
                    str.strip(data['id']),
                    str.strip(data['name']),
                    str.strip(data['description']),
                    data['goals'], # TODO: Добавить тип для целей
                    LevelMapData(
                        data['map']['width'],
                        data['map']['height'],
                        [
                            TilemapLayerData(str.strip(layer['tilemap_id']), layer['tiles']) 
                            for layer in data['map']['tilemap_layers']
                        ]
                    ),
                    [
                        EntityData(entity['type'], entity['name'], entity['x'], entity['y'])
                        for entity in data['entities']
                    ]
                )
                logger.success("'{id}' data loaded", id=level_data.id)
                return level_data
            
        except(KeyError, json.JSONDecodeError, FileNotFoundError) as e:
            messages = {
                KeyError: "Invalid data key",
                json.JSONDecodeError: "Data parsing error",
                FileNotFoundError: "Data file not found"
            }

            logger.exception(messages[type(e)])
            raise LevelError("Error occurred while loading a level")
