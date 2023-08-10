"""This is the base class"""
class Base:
    """Private class attribute"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id        
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
from models.base import Base
"""This is the rectangle class"""          
class Rectangle(Base):
    """This is the getter"""
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y

   