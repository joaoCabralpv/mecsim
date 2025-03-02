import pygame as pg
from pygame.freetype import Font

_font = Font("font.ttf", 15)

class Button:
    rect:pg.rect
    color:pg.color
    text:str
    text_color:pg.color
    font:Font
    parent_surface_position:tuple[int,int]
    event:int

    def __init__(self,rect:pg.rect,color:pg.color,text:str,text_color:pg.color,event:int):
        self.rect=rect
        self.color=color
        self.text=text
        self.text_color=text_color
        self.font=_font
        self.event=event

    def render(self,surface:pg.surface):
        pg.draw.rect(surface,self.color,self.rect)
        text_surface,rect = self.font.render(self.text,self.text_color)
        pos_x=(self.rect.x+((self.rect.w-rect.w)//2))
        pos_y=(self.rect.y+((self.rect.h-rect.h)//2))
        surface.blit(text_surface,(pos_x,pos_y))

    def update(self):
        if pg.mouse.get_just_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos()):
            pg.event.post(pg.event.Event(self.event))

class Side_panel:

    class ButtonWrapper:
        button:Button
        y_pos:int
        def __init__(self, button:Button, y_pos:int):
            self.button=button
            self.y_pos=y_pos

    width:int
    pos:tuple[int,int]
    color:pg.color
    surface:pg.surface
    button_list = list[ButtonWrapper]
    
    def __init__(self,width):
        self.width=width
        self.color=pg.Color(45, 52, 54)
        window_width,height = pg.display.get_surface().get_size()
        self.surface=pg.Surface((self.width,height))
        self.pos = (window_width-self.width,0)
        self.button_list = []
    
    def render(self,surface:pg.surface):
        self.surface.fill(self.color)
        surface.blit(self.surface,self.pos)
        for button in self.button_list:
            button.button.render(surface)
            button.button.update()


    def resize(self):
        window_width,height = pg.display.get_surface().get_size()
        self.surface=pg.Surface((self.width,height))
        self.pos = (window_width-self.width,0)
        for button in self.button_list:
            button.button.rect = pg.Rect(self.pos[0],button.y_pos,self.width,button.button.rect.height)


    def add_button(self,y_pos,height:int,color:pg.color,text:str,text_color:pg.color,event:pg.event):
        rect = pg.Rect(self.pos[0],y_pos,self.width,height)
        self.button_list.append(self.ButtonWrapper(Button(rect,color,text,text_color,event),y_pos))
