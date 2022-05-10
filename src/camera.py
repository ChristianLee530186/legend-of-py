from . import *

class Camera(SDL_Rect):
    def __init__(self, *args):
        super().__init__(*args)
        self.mX = size[0]
        self.mY = size[1]

def updateCamera(data):
    # Move camera

    # Check bounds
    if camera.x < 0:
        camera.x = 0
    elif camera.x > camera.mX:
        camera.x = camera.mX
    if camera.y < 0:
        camera.y = 0
    elif camera.y > camera.mY:
        camera.y = camera.mY
