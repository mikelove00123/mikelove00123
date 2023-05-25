import math

class Vector:
    x=0.0
    y=0.0

    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __add__(self,v):
        return Vector(self.x + v.x, self.y + v.y)

    def __sub__(self,v):
        return Vector(self.x - v.x, self.y - v.y)  

    def __mul__(self,m):
        return Vector(self.x*m, self.y*m)    

    def dot(self,v):
        return self.x*v.x+self.y*v.y   

    def size(self):
        return math.sqrt(self.x**2+self.y**2)

    def unit(self):
        s = self.size()
        return Vector(self.x/s,self.y/s)

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

print(Vector(2,3) +Vector())