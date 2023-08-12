"""This is the rectangle module import"""
from models.rectangle import Rectangle

"""This is the square class inheriting from the rectangle"""


class Square(Rectangle):
    """__init method calls the function"""

    def __init__(self, size, x=0, y=0, id=None):
        """calling the super class using the logic of the Rectangle"""
        super().__init__(size, size, x, y, id)
        self.size = size       
    """str method for printing"""

    def __str__(self):
        """defines the format for returning the square attributes"""
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, x, y, width)

    @property
    def square(size):
        return size.__x

    @square.setter
    def square(self, value):
        self.__size = value

