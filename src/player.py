from . import *

class Player(Actor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def move(self, direction:Direction) -> None:
        pass

    def physics(self) -> None:
        for v in self.velocity:
            if self.velocity[v] > self.speedCap:
                self.velocity[v] = self.speedCap
            elif self.velocity[v] < self.speedCap * -1:
                self.velocity[v] = self.speedCap * -1
        # Apply motion
        self.dstrect.x += self.velocity['vx'] * self.speed
        self.dstrect.y += self.velocity['vy'] * self.speed
