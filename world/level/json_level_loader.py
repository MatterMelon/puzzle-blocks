import json

from core.logging.logger import get_logger
from core.logging.loggger_domain import LoggerDomain
from world.level.exceptions import LevelError
from world.tilemap.tilemap_layer_data import TilemapLayerData

from .level_data import LevelData
from .level_loader import LevelLoader
from .level_map_data import LevelMapData

logger = get_logger(LoggerDomain.LEVEL)

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
                        [
                            TilemapLayerData(str.strip(layer['tilemap_id']), layer['tiles']) 
                            for layer in data['map']['tilemap_layers']
                        ]
                    ),
                    data['entities']
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
