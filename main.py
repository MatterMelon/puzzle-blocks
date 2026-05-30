import sys

import pygame as pg

pg.init()
pg.font.init()

WINDOW_SIZE = (800, 600)
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("PuzzleBlocks")
font = pg.font.SysFont('Arial', 24)
clock = pg.time.Clock()

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
    screen.fill(pg.Color(255,255,255))
    pg.display.flip()
    clock.tick(60)
