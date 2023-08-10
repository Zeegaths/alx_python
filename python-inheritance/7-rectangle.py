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
        """Setting the height and width"""
        super().integer_validator("width", width)
        self._Rectangle__width = width
        super().integer_validator("height", height)
        self._Rectangle__height = height
    def calculate_area(self):
        return self.___width * self.__height

        def __str__(self):
            return f"Rectangle:(width={self._Rectangle__width}, height={self._Rectangle__height})" 
        print(dir(Rectangle))

