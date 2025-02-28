import pygame as pg
from pygame.math import Vector2 as Vector

class Body:
    pos: Vector
    mass: float

    def __init__(self,pos:Vector,mass:float):
        self.pos=pos
        self.mass=mass

    def render(self,screen:pg.surface):
        pg.draw.circle(screen,"white",self.pos,10)
