from vector import Vector
import random

class Rect:
    def __init__(self,canvas):
        self.pos = Vector(
            random.randint(1, 500), random.randint(1, 500))
        self.vel = Vector(
            random.randint(1, 10), random.randint(1, 10))
        self.R = random.randint(1, 255)
        self.G = random.randint(1, 255)
        self.B = random.randint(1, 255)
        self.Size = random.randint(1, 100)
        self.name = str(random.randint(1,100))
        self.canvas = canvas

    def draw(self):
        self.canvas.create_rectangle(
            self.pos.x,
            self.pos.y,
            self.pos.x+self.Size,
            self.pos.y+self.Size,
            fill='#%02x%02x%02x'%(self.R,self.G,self.B), tag=self.name)

    def move(self):
        self.canvas.move(self.name,self.vel.x,self.vel.y)
        self.pos = self.pos+self.vel
        if self.pos.x > 500:
            self.pos.x = 500
            self.vel.x *= -1
        if self.pos.y >500:
            self.pos.y = 500
            self.vel.y *= -1
        if self.pos.x<0:
            self.pos.x=0
            self.vel.x *= -1
        if self.pos.y <0:
            self.pos.y=0
            self.vel.y *= -1