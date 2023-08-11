"""This is the metaclass"""
class metaGeometry(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
"""This is an empty class""" 
class BaseGeometry(metaclass=metaGeometry):
    """This class is empty"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    """area"""    
    def area(self):
        raise Exception("area() is not implemented")
    """integer validator"""
    def integer_validator(self, name, value):   
        """checking instance"""     
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
"""rectangle class"""     
class Rectangle(BaseGeometry(metaclass=metaGeometry)):
    """Rectangle subclass"""
    def __init__(self, width, height):
        """calling the validator method"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height