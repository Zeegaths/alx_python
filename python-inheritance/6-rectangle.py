"""This is the metaclass"""
class metaGeometry(type):
    """
    A custom metaclass to modify class attributes using __dir__.
    """
    def __dir__(cls):
        """
        Modify the list of attributes to exclude __init_subclass__.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

"""This is an empty class"""
class BaseGeometry(metaclass=metaGeometry):
    """
    A base class that defines common geometric operations and validation methods.

    Attributes:
        None

    Methods:
        area(): Raises an exception since it's not implemented.
        integer_validator(name, value): Validates that a value is a positive integer.
    """
    def __dir__(cls):
        """
        Modify the list of attributes to exclude __init_subclass__.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def area(self):
        """
        Raise an exception indicating that this method is not implemented.

        Raises:
            Exception: Always raised with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the attribute being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

"""Rectangle class"""
class Rectangle(BaseGeometry(metaclass=metaGeometry)):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(width, height): Initialize the Rectangle with width and height.
    """
    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
