from dataclasses import dataclass

from pygame.sprite import Group, Sprite


@dataclass
class TilemapLayer:
    tiles: Group[Sprite]
    collision: Group[Sprite]