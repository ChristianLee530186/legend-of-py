from . import *

class Player(Actor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dir = Direction.down

    def move(self, direction:Direction) -> None:
        pass

    def physics(self) -> None:
        pass
