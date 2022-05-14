from . import *

def startUp(map):
    for sheet in spriteSheets: # Load all textures
        for tile in spriteSheets[sheet]:
            if isinstance(tile, Texture):
                tile.load()

    # WARNING: PLEASE FIND AN ALTERNATIVE METHOD TO THIS
    storExec = {}
    with open(os.path.abspath(map), 'r') as module: # Load module as plaintext
        exec(module.read(), storExec, None) # Directly execute module.
    storExec['startMap'](globals())
