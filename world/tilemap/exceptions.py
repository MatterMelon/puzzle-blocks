class TilemapError(Exception):
    pass

class MissingTilemapData(TilemapError):
    pass

class MissingTileData(TilemapError):
    pass