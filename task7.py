#Создайте классы геометрических фигур и реализуйте логику сложения
# между фигурами, например: квадрат + квадрат = прямоугольник, прямоугольник +
# прямоугольник (при равных сторонах = квадрат, если нет, то = прямоугольник), и
# ультимативное задание (необязательно), написать логику сложения треугольников

class Shape:
    def __init__(self, side1 = 0, side2 = 0):
        self.side1 = side1
        self.side2 = side2

    def SumShapes(self, other):
        self.side1 = self.side1 + other.side1

    def Draw(self):
        print(self.side1, self.side2)

class Rectangle(Shape):
    def __init__(self, side1, side2):
        super().__init__(side1, side2)

class Square(Shape):
    def __init__(self, side1):
        super().__init__(side1)
        self.side2 = self.side1

gg = Square(2)
gg.Draw()

bb = Rectangle(8, 2)
bb.Draw()

if gg.side1 == bb.side1:
    gg.side2 += bb.side2
    gg.Draw()

elif gg.side1 == bb.side2:
    gg.side2 += bb.side1
    gg.Draw()

elif gg.side2 == bb.side1:
    gg.side1 += bb.side2
    gg.Draw()

elif gg.side2 == bb.side2:
    gg.side1 += bb.side1
    gg.Draw()

else:
    print("нельзя")