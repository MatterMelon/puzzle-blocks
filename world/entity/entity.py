from pygame import Event
from pygame.sprite import Sprite


class Entity(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
    
    def handele_input(self, e: Event) -> None:
        pass