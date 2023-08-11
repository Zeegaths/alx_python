from models.base import Base

class Rectangle(Base):
    """This class represents a Rectangle, inheriting from the Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): The unique identifier for the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for retrieving the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for setting the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for retrieving the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for setting the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for retrieving the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for setting the x-coordinate of the rectangle's position with validation."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for retrieving the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for setting the y-coordinate of the rectangle's position with validation."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height
