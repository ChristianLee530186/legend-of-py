from . import *

def startUp():
    global actors, textures

    for texture in textures:
        if isinstance(textures[texture], Texture):
            textures[texture].load()

    actors[0].spriteSheet.append(Texture('sprites/player/0.png'))

    for i in range(18):
        for n in range(18):
            tiles.append(Actor(dstrect = SDL_Rect(x = i * 50, y = n * 50, w = 50, h = 50), spriteSheet = [textures['grass'],]))

    for i in range(len(actors)):
        if isinstance(actors[i], Player):
            for n in range(len(actors[i].spriteSheet)):
                actors[i].spriteSheet[n].load()
