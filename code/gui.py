import pygame as pg
from pygame.freetype import Font

class Button:
    rect:pg.rect
    color:pg.color
    text:str
    text_color:pg.color
    font:Font

    def __init__(self,rect:pg.rect,color:pg.color,text:str,text_color:pg.color):
        self.rect=rect
        self.color=color
        self.text=text
        self.text_color=text_color
        self.font=Font("font.ttf", 15)

    def render(self,surface:pg.surface):
        pg.draw.rect(surface,self.color,self.rect)
        text_surface,rect = self.font.render(self.text,self.text_color)
        pos_x=(self.rect.x+((self.rect.w-rect.w)//2))
        pos_y=(self.rect.y+((self.rect.h-rect.h)//2))
        surface.blit(text_surface,(pos_x,pos_y))


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
        window_width,height = pg.display.get_surface().get_size()
        self.surface=pg.Surface((self.width,height))
        self.pos = (window_width-self.width,0)
        self.button_list = []
    
    def render(self,surface:pg.surface):
        self.surface.fill("black")
        for button in self.button_list:
            button.button.render(self.surface)

        surface.blit(self.surface,self.pos)

    def resize(self):
        window_width,height = pg.display.get_surface().get_size()
        self.surface=pg.Surface((self.width,height))
        self.pos = (window_width-self.width,0)


    def add_button(self,y_pos,height:int,color:pg.color,text:str,text_color:pg.color):
        rect = pg.Rect(0,y_pos,self.width,height)
        self.button_list.append(self.ButtonWrapper(Button(rect,color,text,text_color),y_pos))
