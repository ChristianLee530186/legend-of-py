from . import *

# Enums, variables, etc
Direction = enum.Enum('Direction', 'up down left right')

# Functions

def inRange(low:int, high:int, x:int):
    return low <= x and x <= high

# Classes

class Timer():
    def __init__(self):
        self.time = 0
        self.on = False

    def start(self) -> None:
        self.time = time.time()
        self.on = True

    def stop(self) -> None:
        self.on = False

    def getTicks(self) -> float:
        if self.on:
            return time.time() - self.time
        raise Exception('timer is not running')

    def delay(self, fps:int = 30) -> None:
        e = self.getTicks()
        if e < 1 / fps:
            time.sleep(1 / fps - e)

class SDL_Rect():
    def __init__(self, x:int = 0, y:int = 0, w:int = 0, h:int = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def array(self):
        return (
            self.x,
            self.y,
            self.w,
            self.h,
        )

class Texture():
    def __init__(self, path:str):
        self.path = path
        self.data = None

    def load(self) -> None:
        self.data = sdl2.ext.renderer.Texture(renderer, sdl2.ext.image.load_img(self.path))

    def unload(self) -> None:
        sdl2.SDL_DestroyTexture(self.data)
        self.data = None

class Actor():
    def __init__(self, id:uuid.uuid4 = uuid.uuid4(), spriteSheet:list = [], dstrect:SDL_Rect = SDL_Rect(), masks:list = []):
        self.id = id
        self.spriteSheet = spriteSheet
        self.dstrect = dstrect
        self.masks = masks

        # Malleable attributes
        self.spriteIndex = 0
        self.dir = Direction.down
        self.velocity = {
            'vx': 0,
            'vy': 0,
        }
        self.speedIncrement = 0.5
        self.speedCap = 3
        self.speed = 2
