class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_rectangle_char(self):
        return 'Rectangle(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.width) + ', ' + str(self.height) + ')' 

        #Можно ли здесь было использовать форматированные строки?
        # return f'Rectangle({self.x}, {self.y}, {self.width}, {self.height})'
        #Вроде как, если прогнать объект с этим методом через type, тоже будет str

rect_1 = Rectangle(5, 10, 50, 100)

print(rect_1.get_rectangle_char())