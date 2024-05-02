# Python Super 函式

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print("矩形的初始化已執行")
class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
        print("正方形得初始化已執行")

square = Square(5, 5)
print(square.length, square.width)
