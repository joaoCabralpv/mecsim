import pygame as pg
import pygame_gui as gui
from pygame.math import Vector2 as Vector

from body import Body
from force import Force
from vector_tools import *
import gui 

pg.init()
screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)

side_menu = gui.Side_panel(150)
side_menu.add_button(10,30,"red","Show vectors","green")

clock = pg.time.Clock()
running = True

bodyList:list[Body] = []

bodyList.append(Body(Vector(210,210),500))


bodyList[0].apply_force(Force(Vector(3,0)))
while running:
    time_delta = clock.tick(60)/1000.0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.VIDEORESIZE:
            print(event.h)
            side_menu.resize()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cyan")
    # RENDER YOUR GAME HERE
    for body in bodyList:
        body.update()
        body.render(screen)
        body.render_forces(screen)
    side_menu.render(screen)
    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()