import pygame as pg

from draggable import Draggable


class PuzzleBlock(Draggable):
    def __init__(self, x, y, width, heigth, color: tuple):
        super().__init__(x, y, width, heigth)
        # self.__rect = pg.Rect(x, y, width, heigth)
        self.__color = color
        self.__border_radius = 15
    
    def draw(self, surface):
        pg.draw.rect(surface, self.__color, self._rect, border_radius=self.__border_radius)