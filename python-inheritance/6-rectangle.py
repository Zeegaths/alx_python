"""This is an empty class"""
class metaGeometry(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    """This is an empty class"""
class BaseGeometry(metaclass=metaGeometry):
    """This class is empty"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
    """rectangle class"""
class Rectangle(BaseGeometry): 
    """calling the magic method"""   
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
     
    def integer_validator(self, name, value):       
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
