"""This is the rectangle module import"""
from models.rectangle import Rectangle

"""This is the square class inheriting from the rectangle"""


class Square(Rectangle):
    """__init method calls the function"""

    def __init__(self, size, x=0, y=0, id=None):
        """calling the super class using the logic of the Rectangle"""
        super().__init__(size, size, x, y, id)
        self.size = size       
    """str method for pr inting"""

    def __str__(self):
        """defines the format for returning the square attributes"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(width):
        return width.self

    @size.setter
    def size(self, value):
        """validation"""
        if not isinstance(value, int):
            raise TypeError ("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

