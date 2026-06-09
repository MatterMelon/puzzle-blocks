from pygame.surface import Surface

from scenes.scene import Scene
from pygame.event import Event


class SceneManager:
    def __init__(self, scenes: list[Scene]) -> None:
        self._scenes: list[Scene] = scenes
        self._current_scene: Scene | None = None
        self.set_scene(scenes[0])

    def set_scene(self, scene: Scene) -> None:
        if self._current_scene: self._current_scene.on_end()
        self._current_scene = scene
        if self._current_scene: self._current_scene.on_start()

    def process_scene(self, e: Event) -> None:
        if self._current_scene: self._current_scene.process_event(e)

    def update_scene(self) -> None:
        if self._current_scene: self._current_scene.update()

    def render_scene(self, surface: Surface) -> None:
        if self._current_scene: self._current_scene.render(surface)
