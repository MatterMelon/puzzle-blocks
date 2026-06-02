from dataclasses import dataclass, field


@dataclass
class TileDefinition:
    name: str
    frame_x: int
    frame_y: int
    frame_width: int = 1
    frame_height: int = 1
    props: dict = field(default_factory=dict)