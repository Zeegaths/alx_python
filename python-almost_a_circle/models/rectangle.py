from models.base import Base

class Rectangle(Base):
    """This class represents a Rectangle inheriting from the Base class."""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle object.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): Y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): Unique identifier for the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width
        
    @width.setter
    def width(self, width):
        """
        Set the width of the rectangle.

        Args:
            width (int): New width value.
        
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than or equal to 0.
        """   
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")     
        if width <= 0:
            raise ValueError("Width must be > 0")
        self.__width = width
    
    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height
        
    @height.setter
    def height(self, height):
        """
        Set the height of the rectangle.

        Args:
            height (int): New height value.
        
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than or equal to 0.
        """
        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if height <= 0:
            raise ValueError("Height must be > 0")
        self.__height = height
        
    @property
    def x(self):
        """Get the x-coordinate of the rectangle's position."""
        return self.__x
    
    @x.setter
    def x(self, x):
        """
        Set the x-coordinate of the rectangle's position.

        Args:
            x (int): New x-coordinate value.
        
        Raises:
            TypeError: If x is not an integer.
            ValueError: If x is less than 0.
        """
        if not isinstance(x, int):
            raise TypeError("X must be an integer")
        if x < 0:
            raise ValueError("X must be >= 0")
        self.__x = x
        
    @property
    def y(self):
        """Get the y-coordinate of the rectangle's position."""
        return self.__y
    
    @y.setter
    def y(self, y):
        """
        Set the y-coordinate of the rectangle's position.

        Args:
            y (int): New y-coordinate value.
        
        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than 0.
        """
        if not isinstance(y, int):
            raise TypeError("Y must be an integer")
        if y < 0:
            raise ValueError("Y must be >= 0")
        self.__y = y
