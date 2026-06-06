from abc import ABC

from world.entity.entity import Entity


class EntityController(ABC):
    def __init__(self, entity: Entity):
        self.entity = entity
