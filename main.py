import sys

import pygame as pg

from world.level.json_level_loader import JsonLevelLoader
from world.level.level import Level

pg.init()
pg.font.init()

WINDOW_SIZE = (800, 600)
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("PuzzleBlocks")
font = pg.font.SysFont('Arial', 24)
clock = pg.time.Clock()

level_data = JsonLevelLoader.load('./data/levels/level_01.json')
level = Level(level_data)

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
    screen.fill(pg.Color(255,255,255))
    level.draw(screen)
    pg.display.flip()
    clock.tick(60)
