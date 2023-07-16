import pygame
import random
import math

#blueprints
class Door(object):
  def __init__(self, position ):
        pieces = door_color_list[random.randint(0,len(door_color_list)-1)]
        spaces2.append(pieces)
        if pieces not in used2:
            used2.append(pieces)
            door_color_list.remove(pieces)
        self.color = pieces
        self.size = (100,140)
        self.position = (position)
        self.state = 0 #0 = closed state open = 1 open and enlightened = 2
        self.chosen = False
        self.dt = 0
        self.jiggle = False
 
  def  draw(self, window):
        if self.jiggle == True:
            self.dt = (self.dt + 0.001) % 2*math.pi
            x = self.position[0]
            y = self.position[1]
            dy = 3*math.sin(self.dt*180/math.pi)+80
            self.position = (x,dy)

        rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size [1])
        if self.state == 0:
            pygame.draw.rect(window, self.color, rect)
            pygame.draw.rect(window, (0,0,0), rect)
        elif self.state == 1:
            pygame.draw.rect(window, self.color, rect)
        elif self.state == 2:
            pygame.draw.rect(window, self.color, rect, 4)
        elif self.state == 3:
            pass
            
      
    
      

             
        
class Ball(object):
    def __init__(self, position):
        piece = ball_color_list[random.randint(0,len(ball_color_list)-1)]
        spaces.append(piece)
        if piece not in used:
            used.append(piece)
            ball_color_list.remove(piece)
        self.color = piece
        if self.color == [192,192,192]:
            shadow = 6
        if self.color == [255,0,0]:
            shadow = 1
        if self.color == [128,0,0]:
            shadow = 2
        if self.color == [0,255,255]:
            shadow = 3
        if self.color == [224,255,255]:
            shadow = 4
        if self.color == [0,128,128]:
            shadow = 5  
        self.size = (50,50)
        self.position = (position)
        self.energy = shadow
        
    def  draw(self, window):
        ellipse = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size [1])
        pygame.draw.ellipse(window, self.color, ellipse)
        
class Selector(object):
    def __init__(self, x,y,n):
        self.offset = x
        self.x = x
        self.y = y
        self.n = n
        
    def right(self,dis):
        self.x += dis 
        if self.x > dis*self.n+self.offset:
            self.x = self.offset
            
    def left(self, dis):
        self.x += dis*-1
        if self.x <= self.offset-100:
            self.x = dis*self.n+self.offset
            
    def draw(self,window):
        pygame.draw.polygon(window, (0,0,0), [(self.x, self.y),(self.x+25,self.y+40),(self.x+50,self.y)])
        
ball_color_list = [[255,0,0],[0,255,255],[224,255,255],[128,0,0],[0,128,128],[192,192,192]]

spaces = []

used= []

door_color_list = [[255,0,0],[0,255,255],[224,255,255],[128,0,0],[0,128,128]]

used2 = []

spaces2 = []