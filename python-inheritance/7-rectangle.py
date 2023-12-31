"""This is an empty class"""
class metaGeometry(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    """This is an empty class"""
class BaseGeometry(metaclass=metaGeometry):
    """This class is empty"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):        
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        
class Rectangle(BaseGeometry):
    """Rectangle subclass"""
    def __init__(self, width, height):
        """calling the validator method"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """returns the area of the object"""
        return self.__width * self.__height

    def __str__(self):
         """str method for printing"""
         return "[Rectangle] {}/{}".format(self.__width, self.__height) 
    def __dir__(self):
        """
        This function removes the __init_subclass (method) from the default method inherited from the parent class
        """
        return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]

