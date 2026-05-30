import pygame as pg


class Clickable():
    def __init__(self, x, y, width, heigth):
        self._rect = pg.Rect(x, y, width, heigth)
        self.__clicked = False
        self._click_pos = None
        self._offset_x = None
        self._offset_y = None
    
    def on_clicked(self):
        self.__clicked = True
        print("Clicked")

    def on_released(self):
        self.__clicked = False
        print("Released")

    def handle_event(self, event: pg.Event):
        if event.type == pg.MOUSEBUTTONDOWN:
            btn = event.dict['button']
            pos = event.dict['pos']
            if btn == 1 and self._rect.collidepoint(pos):
                self._offset_x = self._rect.x - pos[0]
                self._offset_y = self._rect.y - pos[1]
                self.on_clicked()
        elif event.type == pg.MOUSEBUTTONUP and self.__clicked:
            if event.dict['button'] == 1:
                self.on_released()
        elif event.type == pg.MOUSEMOTION and self.__clicked:
            pos = event.dict['pos']
            if not self._rect.collidepoint(pos):
                self.on_released()