import pygame as pg
from pygame.math import Vector2 as Vector
from force import Force
from vector_tools import *
from ground import *
from math import sin,cos,pi

gravity = 1

class Body:
    rect: pg.Rect
    velocity: Vector
    applied_forces: list[Force]
    net_force: Vector
    normal_force: Vector
    gravitational_force: Vector
    max_friction_magintude: int
    friction_force: Vector
    mass: float


    def __init__(self,rect:pg.Rect,mass:float,velocity=Vector(0,0)):
        self.rect=rect
        self.mass=mass
        self.velocity=velocity
        self.net_force=Vector(0,0)
        self.normal_force=Vector(0,0)
        self.gravitational_force=Vector(0,mass*gravity)
        self.applied_forces = []

    def pos(self):
        return (self.rect.x,self.rect.y)
    
    def center(self):
        return self.rect.center

    def render(self,screen:pg.surface):
        pg.draw.rect(screen,"white",self.rect)

    def render_forces(self,screen:pg.surface):
        draw_vector(screen,self.center(),self.velocity,(255,0,255),scale=5)
        for force in self.applied_forces:
            draw_vector(screen,self.center(),force.direction,(0,0,0))
        self.render_normal_force(screen)
        self.render_gravitational_force(screen)

    def render_net_force(self,screen:pg.surface):
        draw_vector(screen,self.center(),self.net_force,(255,0,0))

    def render_normal_force(self,screen:pg.surface):
        if self.normal_force:
            draw_vector(screen,self.center(),self.normal_force,(0,0,255))

    def render_gravitational_force(self,screen:pg.surface):
            draw_vector(screen,self.center(),self.gravitational_force,(0,255,0))

    def update(self,ground:Ground):
        self.net_force=Vector(0,0)
        for force in self.applied_forces:
            self.net_force+=force.direction
        self.net_force+=self.gravitational_force

        self.handle_collision(ground)
        self.velocity+=self.net_force/self.mass

        new_pos_x=self.rect.x+self.velocity.x
        new_pos_y=self.rect.y+self.velocity.y
        self.rect=pg.Rect(new_pos_x,new_pos_y,self.rect.width,self.rect.height)

    def apply_force(self,force:Force):
        self.applied_forces.append(force)

    def handle_collision(self,ground:Ground):
        if self.rect.clipline(ground.p1,ground.p2):
            angle = pi-ground.angle if ground.increase_right else ground.angle

            net_force_rotated_x = self.net_force.x*cos(angle)+self.net_force.y*sin(angle)
            net_force_rotated_y = -self.net_force.x*sin(ground.angle)+self.net_force.y*cos(ground.angle)


            # Normal force
            normal_rotated_y=min(-net_force_rotated_y,0)
            # normal_rotated_x = 0


            normal_x=-normal_rotated_y*sin(angle)
            normal_y=normal_rotated_y*cos(angle)
            self.normal_force=Vector(normal_x,normal_y)
            if ground.increase_right:
                self.normal_force*=-1
            self.net_force+=self.normal_force

            # Velocity
            velocity_x_rotated=self.velocity.x*cos(angle)+self.velocity.y*sin(angle)
            new_velocity_x=velocity_x_rotated*cos(angle)
            new_velocity_y=velocity_x_rotated*sin(angle)
            self.velocity=Vector(new_velocity_x,new_velocity_y)

        else:
            self.normal_force=Vector(0,0)
            self.friction_force=Vector(0,0)
