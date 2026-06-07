from pygame.surface import Surface

from scenes.scene import Scene
from pygame.event import Event


class SceneManager:
    def __init__(self, scenes: list[Scene]) -> None:
        self._scenes: list[Scene] = scenes
        self.current_scene: Scene = self._scenes[0]

    def set_scene(self, scene: Scene) -> None:
        self._scenes.append(scene)

    def process_scene(self, e: Event) -> None:
        self.current_scene.process_event(e)

    def update_scene(self) -> None:
        self.current_scene.update()

    def render_scene(self, surface: Surface) -> None:
        self.current_scene.render(surface)