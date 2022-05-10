from . import *

def render():
    for actor in actors:
        actor.dstrect.x -= camera.x
        actor.dstrect.y -= camera.y
        renderer.copy(actor.spriteSheet[actor.spriteIndex].data, dstrect = actor.dstrect.array())
