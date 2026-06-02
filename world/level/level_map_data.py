from dataclasses import dataclass

from tilemap.tilemap_layer_data import TilemapLayerData


@dataclass
class LevelMapData:
    width: int
    height: int
    tilemap_layers: TilemapLayerData