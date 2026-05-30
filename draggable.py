import pygame as pg

from clickable import Clickable


class Draggable(Clickable):
    def __init__(self, x, y, width, heigth):
        super().__init__(x, y, width, heigth)
        self.__is_draging = False

    def on_clicked(self):
        super().on_clicked()
        self.__is_draging = True

    def on_released(self):
        super().on_released()
        self.__is_draging = False
    
    def handle_event(self, event: pg.Event):
        super().handle_event(event)
        if event.type == pg.MOUSEMOTION and self.__is_draging:
            pos = event.dict['pos']
            self._rect.x = pos[0] + self._offset_x
            self._rect.y = pos[1] + self._offset_y

        # if event.type == pg.MOUSEBUTTONDOWN:
        #     btn = event.dict['button']
        #     pos = event.dict['pos']
        #     if btn == 1 and self._rect.collidepoint(pos):
        #         self.__offset_x = self._rect.x - pos[0]
        #         self.__offset_y = self._rect.y - pos[1]
        #         self.__is_draging = True
        # elif event.type == pg.MOUSEBUTTONUP:
        #     btn = event.dict['button']
        #     if btn == 1 and self.__is_draging:
        #         self.__is_draging = False
        # elif event.type == pg.MOUSEMOTION and self.__is_draging:
        #     
            