"""This is an empty class"""


class metaGeometry(type):
    """This is the metaclass"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__()
                if attribute != '__init_subclass__']


"""This is an empty class"""


class BaseGeometry(metaclass=metaGeometry):
    """This is an empty class"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__()
                if attribute != '__init_subclass__']

    def area(self):
        """Calculates the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle subclass"""

    def __init__(self, width, height):
        """Initializes a Rectangle instance"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a formatted string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __dir__(cls):
        """
        Removes the __init_subclass (method)
        from the default method inherited from the parent class
        """
        return [attribute for attribute in super().__dir__()
                if attribute != "__init_subclass__"]


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
