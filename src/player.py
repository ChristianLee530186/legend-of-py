from . import *

class Player(Actor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.modelStage = 0

    def physics(self) -> None:
        for v in self.velocity:
            if self.velocity[v] > self.speedCap:
                self.velocity[v] = self.speedCap
            elif self.velocity[v] < self.speedCap * -1:
                self.velocity[v] = self.speedCap * -1
        # Apply motion
        self.dstrect.x += self.velocity['vx'] * self.speed
        self.dstrect.y += self.velocity['vy'] * self.speed

    def changeModel(self) -> None:
        offSet = 0
        if self.velocity['vy'] > 0:
            offSet = 0
        elif self.velocity['vy'] < 0:
            pass
        if self.velocity['vx'] > 0:
            pass
            #offSet = 3
        elif self.velocity['vx'] < 0:
            pass

        if self.velocity['vx'] != 0 or self.velocity['vy'] != 0:
            self.modelStage += 0.1
            if self.modelStage >= 3:
                self.modelStage = 1
        else:
            self.modelStage = 0

        self.spriteIndex = offSet + int(self.modelStage)
