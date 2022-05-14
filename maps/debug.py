if __name__ == '__main__':
    quit('You cannot directly load a map as a Python file. Please run in tandem with the engine.')

# Always begin map with function "startMap(globals)"
def startMap(ctx): # ctx is the current context of the engine as of the calling of this function in `src/start.py`
    for i in ctx: # This is a customary (although unnecessary) for loop that allows using the same global variables as the engine files
        globals()[i] = ctx[i]

    # Begin the writing of the map
    for i in range(20):
        for n in range(20):
            tiles.append(Actor(dstrect = SDL_Rect(x = i * (size[1] / 10), y = n * (size[1] / 10), w = (size[1] / 10), h = (size[1] / 10)), spriteSheet = 'tiles', spriteIndex = random.randint(0,2)))
