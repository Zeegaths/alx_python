"""models/rectangle.py"""
from models.base import Base

"""This is the rectangle class"""


class Rectangle(Base):
    """calling the superclass and assigning attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """This is the width getter"""
    @property
    def width(self):
        return self.__width

    """width setter"""
    @width.setter
    def width(self, value):
        """validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """This is the height getter"""
    @property
    def height(self):
        return self.__height

    """height setter"""
    @height.setter
    def height(self, value):
        """validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """This is the x getter"""
    @property
    def x(self):
        return self.__x

    """x setter"""
    @x.setter
    def x(self, value):
        """validation"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """This is the y getter"""
    @property
    def y(self):
        return self.__y

    """y setter"""
    @y.setter
    def y(self, value):
        """validation"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    """area of the rectangle"""

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height
    """This is a public method"""
    def display(self):
        """It prints in stdout #"""
        for row in range(self.__height):
            for column in range(self.__width):
                print("#", end="")
            print()  # Print a new line after each row

    def __str__(self):
        """"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.__id, self.__x, self.__y, self.__width, self.__height)

                        

