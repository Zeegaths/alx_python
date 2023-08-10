"""models/rectangle.py"""
from models.base import Base

"""This is the rectangle class"""
class Rectangle(Base):
    """calling the superclass and assigning attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """This is the width getter"""
    @property
    def width(self):
        return self.__width
        
    
    """width setter"""
    @width.setter
    def width(self, width):
        """validation"""   
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")     
        if width <= 0:
            raise ValueError("Width must be > 0")
        self.__width = width
    
    """This is the height getter"""
    @property
    def height(self):
        return self.__height
        
    """height setter"""
    @height.setter
    def height(self, height):
        """validation"""
        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if height <= 0:
            raise ValueError("Height must be > 0")
        self.__height = height
        
    """This is the x getter"""
    @property
    def x(self):
        return self.__x
    
    """x setter"""
    @x.setter
    def x(self, x):
        """validation"""
        if not isinstance(x, int):
            raise TypeError("X must be an integer")
        if x < 0:
            raise ValueError("X must be >= 0")
        self.__x = x
        
    """This is the y getter"""
    @property
    def y(self):
        return self.__y
    
    """y setter"""
    @y.setter
    def y(self, y):
        """validation"""
        if not isinstance(y, int):
            raise TypeError("Y must be an integer")
        if y < 0:
            raise ValueError("Y must be >= 0")
        self.__y = y
