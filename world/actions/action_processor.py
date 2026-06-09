from pygame.sprite import LayeredUpdates

from world.actions.move_action import MoveAction
from world.level.collision_resolver import CollisionResolver


class ActionProcessor:
    def __init__(self, entities: LayeredUpdates, collision_resolver: CollisionResolver) -> None:
        self._entities: LayeredUpdates = entities
        self._collision_resolver: CollisionResolver = collision_resolver

    def update(self) -> None:
        for entity in self._entities:
            action = entity.get_action()
            # TODO: Реализовать соблюдение OCP при разрастании match-case
            # релизовать Action Handler и ActionHandlerRegistry
            # Action -> ActionHandler -> ActionHandlerRegistry -> ActionProcessor
            match action:
                case MoveAction():
                    if self._collision_resolver.can_move(entity, action.dx, action.dy):
                        entity.move_to(action.dx, action.dy)