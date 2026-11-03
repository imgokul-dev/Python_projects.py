
class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclass must implement area()")

    def describe(self):
        return f"{self.name} area: {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        super(). __init__ ("Circle")
        self.radius = radius

    def area (self):
        return 3.14159 * self.radius **2

rect = Rectangle(5,3)
circ = Circle(4)

print(rect.describe())
print(circ.describe())





















