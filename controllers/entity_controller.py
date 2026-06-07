from abc import ABC

from controllers.controller import Controller
from world.entity.entity import Entity


class EntityController(Controller, ABC):
    def __init__(self, entity: Entity):
        self.entity = entity
