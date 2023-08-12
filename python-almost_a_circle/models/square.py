"""This is the rectangle module import"""
from rectangle import Rectangle

"""This is the square class inheriting from the rectangle"""


class Square(Rectangle):
    """__init method calls the function"""

    def __init__(self, size, x=0, y=0, id=None):
        """calling the super class using the logic of the Rectangle"""
        super().__init__(id)
        self.size = size
        self.x = x
        self.y = y
    """str method for printing"""

    def __str__(self):
        """defines the format for returning the square attributes"""
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__size)
