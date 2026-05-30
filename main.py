import pygame as pg

from puzzle_block import PuzzleBlock

pg.init()
pg.font.init()

WINDOW_SIZE = (800, 600)
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("Andy's game!")
font = pg.font.SysFont('Arial', 24)
clock = pg.time.Clock()

# text_surface = font.render("Text", True, pg.Color(255, 255, 255))
# text_rect = text_surface.get_rect(center = rect_obj.center)

block_1 = PuzzleBlock(100, 100, 200, 100, (0, 0, 0))
block_2 = PuzzleBlock(100, 300, 200, 100, (0, 0, 0))
blocks = [block_1, block_2]


while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
        for block in blocks:
            block.handle_event(e)
        
    screen.fill(pg.Color(255,255,255))
    # pg.draw.rect(screen, pg.Color(0, 0, 0), rect_obj, border_radius=15)
    # screen.blit(text_surface, text_rect)
    for block in blocks:
        block.draw(screen)
    pg.display.flip()
    clock.tick(60)
