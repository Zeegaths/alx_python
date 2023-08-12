"""This is the Rectangle module
"""

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """Square subclass"""

    def __init__(self, size):
        """Initializes a Square instance"""
        super().integer_validator("size", size)
        self.__size = size
        Square = 0

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a formatted string representation of the square"""
        return Square.area

    def __dir__(cls):
        """
        Removes the __init_subclass (method)
        from the default method inherited from the parent class
        """
        return [attribute for attribute in super().__dir__()
                if attribute != "__init_subclass__"]
