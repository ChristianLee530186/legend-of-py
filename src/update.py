from . import *

def update(data):
    updatePlayer(data)

    updateCamera(data)

def updateCamera(data):
    # Move camera
    camera.x = (plr.dstrect.x + plr.dstrect.w / 2) - size[0] / 2
    camera.y = (plr.dstrect.y + plr.dstrect.h / 2) - size[1] / 2
    # Check bounds
    if camera.x < 0:
        camera.x = 0
    elif camera.x > camera.mX:
        camera.x = camera.mX
    if camera.y < 0:
        camera.y = 0
    elif camera.y > camera.mY:
        camera.y = camera.mY

def updatePlayer(data):
    for i in (('vy',sdl2.SDL_SCANCODE_DOWN,sdl2.SDL_SCANCODE_UP),('vx',sdl2.SDL_SCANCODE_RIGHT,sdl2.SDL_SCANCODE_LEFT)):
        if data['keystate'][i[1]]:
            plr.velocity[i[0]] += plr.speedIncrement
        elif data['keystate'][i[2]]:
            plr.velocity[i[0]] -= plr.speedIncrement
        else:
            if abs(plr.velocity[i[0]]) - plr.speedIncrement / 2 < plr.speedIncrement:
                plr.velocity[i[0]] = 0
            if plr.velocity[i[0]] > 0:
                plr.velocity[i[0]] -= plr.speedIncrement / 2
            elif plr.velocity[i[0]] < 0:
                plr.velocity[i[0]] += plr.speedIncrement / 2

    plr.physics()
    plr.changeModel()
