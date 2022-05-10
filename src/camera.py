from . import *

class Camera(SDL_Rect):
    def __init__(self, *args):
        super().__init__(*args)
        self.mX = size[0]
        self.mY = size[1]
