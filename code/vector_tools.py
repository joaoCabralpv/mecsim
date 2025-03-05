import pygame as pg
from pygame.math import Vector2 as Vector
import math

default_scale = 10

def draw_vector(screen,pos:Vector,vector:Vector,color,scale:int=default_scale):
    vector = Vector(vector.x*scale,vector.y*scale)
    end = pos+vector
    head_size=10
    pg.draw.line(screen,color,pos,end,2)
    rotation = (math.atan2(pos[1]-end[1], end[0]-pos[0]))+(math.pi/2)
    two_pi_thirds = 2*math.pi/3
    pg.draw.polygon(screen, color, 
                    ((end[0]+head_size*math.sin(rotation), 
                      end[1]+head_size*math.cos(rotation)), 
                      (end[0]+head_size*math.sin(rotation-two_pi_thirds), 
                       end[1]+head_size*math.cos(rotation-two_pi_thirds)), 
                       (end[0]+head_size*math.sin(rotation+two_pi_thirds), 
                        end[1]+head_size*math.cos(rotation+two_pi_thirds))))
