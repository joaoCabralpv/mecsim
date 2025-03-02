import pygame as pg
import pygame_gui as gui
from pygame.math import Vector2 as Vector
pg.init()

from body import Body
from force import Force
from vector_tools import *
import gui 
from custom_event import *

screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)

side_menu = gui.Side_panel(150)
side_menu.add_button(10,30,pg.Color(178, 190, 195),"Show forces",pg.Color(0, 0, 0),show_forces_event)

clock = pg.time.Clock()
running = True

bodyList:list[Body] = []

bodyList.append(Body(Vector(210,210),500))


bodyList[0].apply_force(Force(Vector(3,0)))

show_forces=False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.VIDEORESIZE:
            print(event.h)
            side_menu.resize()
        if event.type == show_forces_event:
            show_forces = not show_forces
            print(show_forces)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cyan")
    # RENDER YOUR GAME HERE
    for body in bodyList:
        body.update()
        body.render(screen)
        if show_forces:
            body.render_forces(screen)
    side_menu.render(screen)
    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()