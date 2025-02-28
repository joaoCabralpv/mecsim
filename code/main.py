import pygame as pg
from pygame.math import Vector2 as Vector

from body import Body
from force import Force
from vector_tools import *

pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True

bodyList:list[Body] = []

bodyList.append(Body(Vector(100,100),500))

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cyan")
    bodyList[0].apply_force(Force(Vector(0.5,0)))
    # RENDER YOUR GAME HERE
    for body in bodyList:
        body.update()
        body.render(screen)
        body.render_forces(screen)
        

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()