from core.logging.logger import LoggerDomain, get_logger

from pygame.sprite import Group

from world.entity.entity import Entity

logger = get_logger(LoggerDomain.LEVEL)

class CollisionResolver:
    def __init__(self, collision_group):
        self.collision_group: Group = collision_group

    def update_collision(self, collision_group: Group) -> None:
        self.collision_group = collision_group

    def can_move(self, entity: Entity, dx: int, dy: int) -> bool:
        if entity is None:
            return False

        if self.collision_group is None:
            return True

        moved_rect = entity.rect.move(dx, dy)

        for collider in self.collision_group:
            if moved_rect.colliderect(collider.rect):
                logger.info(f"Entity: {entity} collided with {collider}")
                return False

        return True