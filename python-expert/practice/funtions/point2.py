import math
class Point():
    x=0.0
    y=0.0
    def __init__(self):
        self.x=0
        self.y=0   
    def __init__(self,x,y):
        self.x=x
        self.y=y
 
    def distanceTo(self,p):
        return math.sqrt(p.x-self.x)**2+(p.y-self.y**2)
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def __add__(self,other):
        return Point(p.x+self.x, p.y+self.y)

p= Point(1, 2)
q= Point(5, 10)

print(p.distanceTo(q))

print(Point.distanceTo(p, q))

print(p)
print(p+q)