# Xây dựng lớp cha 
class Shape():
    def __init__(self, color, shape) -> None:
        self.color = color
        self.shape = shape

# Xây dựng lớp con Circle
# class <Tên lớp con>(<Tên lớp cha>)
class Circle(Shape):
    def __init__(self, color, shape, width) -> None:
        super().__init__(color, shape)
        self.width = width

    def getArea(self):
        return self.width * 3.14
    
class Rectagle(Shape):
    def __init__(self, color, shape, width, height) -> None:
        super().__init__(color, shape)
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height 