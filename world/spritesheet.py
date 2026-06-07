import pygame as pg
from pygame import Surface


class SpriteSheet:
    def __init__(self, file_path: str, grid_size: int):
        self.__sheet = pg.image.load(file_path)
        self.__grid_size = grid_size

    def get_grid_size(self) -> int:
        return self.__grid_size
    
    def get_image(self, frame_x, frame_y, frame_width=1, frame_height=1) -> Surface:
        rect = pg.Rect(frame_x * self.__grid_size, frame_y * self.__grid_size, self.__grid_size * frame_width, self.__grid_size * frame_height)
        image = self.__sheet.subsurface(rect)
        return image.convert_alpha()

    def load_strip(self, rect, image_count) -> list[Surface]:
        tup = [(rect[0] + rect[2] * i, rect[1], rect[2], rect[3])
               for i in range(image_count)]
        return [self.get_image(*frame) for frame in tup]