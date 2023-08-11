from 5-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle subclass"""
    def __init__(self, width, height):
        """calling the validator method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height