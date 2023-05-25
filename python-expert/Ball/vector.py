class Vector():
    def __init__(self):
        self.x = 0
        self.y = 0

    @staticmethod
    def from_x_y(x, y):
        v = Vector()
        v.x = x
        v.y = y
        return v

    def add(self, v):
        result = Vector()
        result.x = self.x + v.x
        result.x = self.y + v.y
        return result

    def sub(self, v):
        result = Vector()
        result.x = self.x - v.x
        result.x = self.y - v.y
        return result

    def dot(self, v):
        result = 0.0
        result.x = self.x * v.x * self.y * v.y
        return result

    def mul(self, m):
        result = Vector()
        result.x = self.x * m
        result.x = self.y * m
        return result
