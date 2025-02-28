import pygame as pg
from pygame.math import Vector2 as Vector

class Force:
    direction:Vector

    def __init__(self,vector:Vector):
        self.direction=vector