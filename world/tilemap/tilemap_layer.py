from dataclasses import dataclass

from .tilemap import Tilemap
from .tilemap_layer_data import TilemapLayerData


@dataclass
class TilemapLayer:
    tilemap: Tilemap
    tiles: TilemapLayerData