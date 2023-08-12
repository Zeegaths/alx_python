from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        """"""
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__size)
