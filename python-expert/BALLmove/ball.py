from vector import Vector
import random

class Ball:
    def __init__(self):
        self.pos = Vector(
            random.randint(1, 500), random.randint(1, 500))
        self.vel = Vector(
            random.randint(1, 10), random.randint(1, 10))
        self.R = random.randint(1, 255)
        self.G = random.randint(1, 255)
        self.B = random.randint(1, 255)
        self.Size = random.randint(1, 100)
        self.name = str(random.randint(1,100))
    
    def move(self):
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