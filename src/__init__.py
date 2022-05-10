# External libraries
import os, sys, time, uuid, enum
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
textures = { # Standard tile size for map building will most likely be (HEIGHT / 18)
    'grass': Texture(os.path.abspath('maps/_tilesets/grass.png')),
    'dirt': Texture(os.path.abspath('maps/_tilesets/dirt.png')),
}
player = Player(dstrect = SDL_Rect(w = 50, h = 50))
actors = [player,]
tiles = []
timer = Timer()
camera = Camera(0, 0, *size)

# Updating and rendering modules
from .start import * # StartUp
from .update import * # Update
from .render import * # Render
