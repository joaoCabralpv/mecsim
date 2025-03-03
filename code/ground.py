import pygame as pg
from math import tan

class Ground:
    y_pos:int
    angle:int
    increase_right:bool

    def __init__(self,y_pos:int,angle:int,increase_right):
        self.y_pos=y_pos
        self.angle=angle
        self.increase_right=increase_right

    def render(self,screen:pg.surface):
        window_width = pg.display.get_surface().get_size()[0]
        window_height = pg.display.get_surface().get_size()[1]
        x_pos = (window_height-self.y_pos)/tan(self.angle)
        x_pos = pg.display.get_surface().get_size()[0]-x_pos if self.increase_right else x_pos

        pg.draw.polygon(screen,"white",[ (window_width,self.y_pos) if  self.increase_right  else (0,self.y_pos) ,(x_pos,window_height),pg.display.get_surface().get_size() if self.increase_right else (0,window_height)])

        #pg.draw.line(screen,"red",(x_pos,window_height),(0,self.y_pos))