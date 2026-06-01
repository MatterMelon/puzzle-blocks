import sys

import pygame as pg

from world.levels.json_level_loader import JsonLevelLoader
from world.tilemaps.base_tile_map import BaseTileMap

pg.init()
pg.font.init()

WINDOW_SIZE = (800, 600)
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("PuzzleBlocks")
font = pg.font.SysFont('Arial', 24)
clock = pg.time.Clock()

tilemap = BaseTileMap()

for i in range(100):
    for j in range(100):
        tilemap.place_tile(tilemap.TileType.WALL, i, j, True)
    
data = JsonLevelLoader.load('./data/levels/level_01.json')
print(data)

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
    screen.fill(pg.Color(255,255,255))
    tilemap.draw_tiles(screen)
    # screen.blit(image, image_pos)
    pg.display.flip()
    clock.tick(60)
