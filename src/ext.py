from . import *

class Timer():
    def __init__(self):
        self.start = 0
        self.on = False

    def start(self) -> None:
        self.start = time.time()
        self.on = True

    def stop(self) -> None:
        self.on = False

    def getTicks(self) -> float:
        return time.time() - self.start
