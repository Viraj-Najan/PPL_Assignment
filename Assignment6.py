import turtle

s = turtle.getscreen()
t = turtle.Turtle()


class shape:
    def __init__(self, sides = 0, length = 0) :
        self.sides = sides
        self.length = length


class polygon(shape):
    def info(self):
        print("In geometry, a polygon can be defined as a flat or plane, two-dimensional  with straight sides.")
        
class square(polygon):
    def show(self):
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
        t.fd(self.length)
        t.rt(90)
    

class pentagon(polygon):
    def show(self):
        for i in range(5):
           t.forward(self.length) 
           t.right(72) 

class hexagon(polygon):
    def show(self):
        for i in range(6):
           t.forward(self.length) 
           t.right(60)

class octagon(polygon):
    def show(self):
        for i in range(6):
           t.forward(self.length) 
           t.right(45)

class triangle(polygon):
    def show(self):
        t.forward(self.length) 
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)


hex1 = hexagon(6, 100)
hex1.info()
hex1.show()






