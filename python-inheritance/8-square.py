class MetaGeometry(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class BaseGeometry(metaclass=MetaGeometry):
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
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    @classmethod
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        Square = 0

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return str(Square.area)

    @classmethod
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != "__init_subclass__"]
