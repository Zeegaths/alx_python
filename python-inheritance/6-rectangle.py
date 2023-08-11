"""This is the base class"""
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    """Integer validator"""
    def integer_validator(self, name, value):
        """instances"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
"""class rectangle"""
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
