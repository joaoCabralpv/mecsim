import pygame as pg
import pygame_gui as gui
from pygame.math import Vector2 as Vector
pg.init()

from body import Body
from force import Force
from vector_tools import *
import gui 
from custom_event import *
from mode import *


screen = pg.display.set_mode((1280, 720), pg.RESIZABLE)

side_menu = gui.Side_panel(150)
side_menu.add_button(5,30,pg.Color(178, 190, 195),"Show forces",pg.Color(0, 0, 0),show_forces_event)
side_menu.add_button(40,30,pg.Color(178, 190, 195),"Add force",pg.Color(0, 0, 0),add_force_event)

clock = pg.time.Clock()
running = True

bodyList:list[Body] = []

bodyList.append(Body(pg.Rect(100,100,100,50),500))


#bodyList[0].apply_force(Force(Vector(3,0)))

body_to_add_force = None

pos_to_add_body = None

show_forces=True

while running:

    screen.fill("cyan")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.VIDEORESIZE:
            side_menu.resize()
        elif event.type == show_forces_event:
            show_forces = not show_forces
        elif event.type == add_force_event:
            mode=Mode.ADD_FORCE_SELECT_OBJECT
        elif event.type == add_body_event:
            mode=Mode.ADD_BODY_SELECT_POSITION


    if mode == Mode.ADD_FORCE_SELECT_OBJECT and pg.mouse.get_just_pressed()[0]:
        for body in bodyList:
            if body.rect.collidepoint(pg.mouse.get_pos()):
                body_to_add_force=body
                mode=Mode.ADD_FORCE_CHOSE_VECTOR
                break

    elif mode == Mode.ADD_FORCE_CHOSE_VECTOR:
        if pg.mouse.get_just_pressed()[0]:
            body_pos=body_to_add_force.center()
            mouse_pos=pg.mouse.get_pos()
            force=Force((Vector(mouse_pos)-Vector(body_pos))/10)
            body_to_add_force.apply_force(force)
            mode=Mode.DEFAULT

        draw_vector(screen,body_to_add_force.center(),(Vector(pg.mouse.get_pos())-Vector(body_to_add_force.center()))/scale,(0,0,0))


    # fill the screen with a color to wipe away anything from last frame
    
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