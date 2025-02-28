import pygame as pg
from pygame.math import Vector2 as Vector
from force import Force
from vector_tools import *

class Body:
    pos: Vector
    velocity: Vector
    applied_forces: list[Force]
    net_force: Vector
    mass: float

    def __init__(self,pos:Vector,mass:float,velocity=Vector(0,0)):
        self.pos=pos
        self.mass=mass
        self.velocity=velocity
        self.net_force=Vector(0,0)
        self.applied_forces=[]

    def render(self,screen:pg.surface):
        pg.draw.circle(screen,"white",self.pos,10)

    def render_forces(self,screen:pg.surface):
        for force in self.applied_forces:
            draw_vector(screen,self.pos,force.direction,(0,0,0))

    def update(self):
        self.velocity+=self.net_force/self.mass
        self.pos+=self.velocity

    def apply_force(self,force:Force):
        self.applied_forces.append(force)
        self.net_force+=force.direction