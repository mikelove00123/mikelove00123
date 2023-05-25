import random
import vector
from graphics import *

class Ball():
    def __init__(self):
        self.R = random.randrange(0,255)
        self.G = random.randrange(0,255)
        self.B = random.randrange(0,255)
        self.Size = random.randrange(0,50)
        self.pos = vector.Vector()
        self.pos.x = random.randrange(0,500)
        self.pos.y = random.randrange(0,500)
        self.vel = vector.Vector()
        self.vel.x = random.randrange(0,5)-3
        self.vel.y = random.randrange(0,5)-3

        self.c = Circle(Point(self.pos.x, self.pos.y), self.Size)
        self.c.setFill(color_rgb(self.R,self.G,self.B))

    def move(self):
        pos_old = self.pos
        self.pos = self.pos.add(self.vel)
        self.c.move(self.pos.x - pos_old.x , self.pos.y - pos_old.y)
    
    def draw(self,win):
        self.c.draw(win)