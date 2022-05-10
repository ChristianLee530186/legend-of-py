from . import *

def getInputs():
    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            quit()
    # Keys
    keystate = sdl2.SDL_GetKeyboardState(None) # Run key inputs
    if keystate[sdl2.SDL_SCANCODE_ESCAPE]:
        quit()
    return {
        'keystate': keystate,
        'events': events,
    }
