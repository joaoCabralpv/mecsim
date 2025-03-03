import pygame as pg
from pygame.math import Vector2 as Vector
from force import Force
from vector_tools import *

class Body:
    rect: pg.Rect
    velocity: Vector
    applied_forces: list[Force]
    net_force: Vector
    mass: float

    def __init__(self,rect:pg.Rect,mass:float,velocity=Vector(0,0)):
        self.rect=rect
        self.mass=mass
        self.velocity=velocity
        self.net_force=Vector(0,0)
        self.applied_forces=[]

    def pos(self):
        return (self.rect.x,self.rect.y)
    
    def center(self):
        return self.rect.center

    def render(self,screen:pg.surface):
        pg.draw.rect(screen,"white",self.rect)

    def render_forces(self,screen:pg.surface):
        for force in self.applied_forces:
            draw_vector(screen,self.center(),force.direction,(0,0,0))

    def render_net_force(self,screen:pg.surface):
        draw_vector(screen,self.center(),self.net_force,(255,0,0))

    def update(self):
        self.velocity+=self.net_force/self.mass
        new_pos_x=self.rect.x+self.velocity.x
        new_pos_y=self.rect.y+self.velocity.y
        self.rect=pg.Rect(new_pos_x,new_pos_y,self.rect.width,self.rect.height)

    def apply_force(self,force:Force):
        self.applied_forces.append(force)
        self.net_force+=force.direction