import pygame as pg
import pygame_gui as gui
from pygame.math import Vector2 as Vector
from math import tau

pg.init()

from body import Body
from force import Force
from vector_tools import *
import gui 
from custom_event import *
from state import *
from ground import Ground

resolution = (1280, 720)
screen = pg.display.set_mode(resolution, pg.RESIZABLE)

side_menu = gui.Side_panel(150)
side_menu.add_button(5,30,pg.Color(178, 190, 195),"Show forces",pg.Color(0, 0, 0),show_forces_event)
side_menu.add_button(40,30,pg.Color(178, 190, 195),"Add force",pg.Color(0, 0, 0),add_force_event)

clock = pg.time.Clock()
running = True

bodyList.append(Body(pg.Rect(100,100,100,50),500))

ground = Ground(400,tau/16,True)

body_to_add_force = None

pos_to_add_body = None

while running:

    screen.fill("cyan")

    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                paused = not paused
        elif event.type == pg.VIDEORESIZE:
            resolution=pg.display.get_surface().get_size()
            side_menu.resize()
        elif event.type == show_forces_event:
            show_forces = not show_forces
        elif event.type == add_force_event:
            mode=Mode.ADD_FORCE_SELECT_OBJECT

    # Update body and forces
    ground.render(screen)
    for body in bodyList:
        if not paused:
            body.update()
        body.render(screen)
        if show_forces:
            body.render_forces(screen)
            body.render_net_force(screen)
    side_menu.render(screen)

    # Handle difrent modes
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
            force=Force((Vector(mouse_pos)-Vector(body_pos))/scale)
            body_to_add_force.apply_force(force)
            mode=Mode.DEFAULT

        draw_vector(screen,body_to_add_force.center(),(Vector(pg.mouse.get_pos())-Vector(body_to_add_force.center()))/scale,(0,0,0))

    # Display things
    pg.display.flip()
    clock.tick(60)  

pg.quit()