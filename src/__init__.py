# External libraries
import os, sys, time, uuid, enum, random, copy
import sdl2, sdl2.ext

#
name = 'Legend of Py'
version = 0.1

# SDL2 objects
size = (900, 900)
window = sdl2.ext.Window(
    title = name + ' v' + str(version),
    position = (0, 0),
    size = size, flags = (
        sdl2.SDL_WINDOW_SHOWN# | sdl2.SDL_WINDOW_FULLSCREEN
    )
)
renderer = sdl2.ext.renderer.Renderer(
    target = window,
    logical_size = size,
    flags = (
        sdl2.SDL_RENDERER_ACCELERATED
    )
)

# Module files
from .ext import *
from .player import *
from .world import *
from .camera import *
from .inputs import *

# Game Objects
spriteSheets = {
    'tiles': ( # Standard tile size for map building will most likely be (HEIGHT / 10)
        Texture(os.path.abspath('maps/_tilesets/grass1.png')),
        Texture(os.path.abspath('maps/_tilesets/grass2.png')),
        Texture(os.path.abspath('maps/_tilesets/grass3.png')),
        Texture(os.path.abspath('maps/_tilesets/dirt.png')),
    ),
    'player': [ Texture('sprites/player/%s.png' % i) for i in range(1) ],
}

plr = Player(dstrect = SDL_Rect(w = size[1] / 9, h = size[1] / 9), spriteSheet = 'player')
actors = [plr,]
tiles = []
timer = Timer()
camera = Camera(0, 0, *size)

# Updating and rendering modules
from .start import * # StartUp
from .update import * # Update
from .render import * # Render
