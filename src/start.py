from . import *

def startUp():
    global actors, textures

    for texture in textures:
        if isinstance(textures[texture], Texture):
            textures[texture].load()

    plr.spriteSheet.append(Texture('sprites/player/0.png'))

    for i in range(20):
        for n in range(20):
            tiles.append(Actor(dstrect = SDL_Rect(x = i * (size[1] / 10), y = n * (size[1] / 10), w = (size[1] / 10), h = (size[1] / 10)), spriteSheet = [textures['grass' + str(random.randint(1,3))],]))

    for i in range(len(actors)):
        if isinstance(actors[i], Player):
            for n in range(len(actors[i].spriteSheet)):
                actors[i].spriteSheet[n].load()
