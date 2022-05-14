from . import *

def render():
    # Clear
    renderer.clear()

    # Render map
    for tile in tiles:
        dstrect = copy.copy(tile.dstrect)
        dstrect.x -= camera.x
        dstrect.y -= camera.y
        renderer.copy(spriteSheets[tile.spriteSheet][tile.spriteIndex].data, dstrect = dstrect.array())

    # Render player
    for actor in actors:
        dstrect = copy.copy(actor.dstrect)
        dstrect.x -= camera.x
        dstrect.y -= camera.y
        renderer.copy(spriteSheets[actor.spriteSheet][actor.spriteIndex].data, dstrect = dstrect.array())

    # Flip backbuffer
    renderer.present()
