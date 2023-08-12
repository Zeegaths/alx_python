"""Import the Rectangle module"""
from rectangle import Rectangle
"""
Define the Square class, which inherits from the Rectangle class"""
class Square(Rectangle):
    """
    This is the Square class, inheriting from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object with the specified attributes.

        :param size: The size of the square's sides.
        :type size: int
        :param x: The x-coordinate position of the square, defaults to 0.
        :type x: int
        :param y: The y-coordinate position of the square, defaults to 0.
        :type y: int
        :param id: The unique identifier of the square, defaults to None.
        :type id: int or None
        """
        super().__init__(id)  # Call the parent class's constructor
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        """
        Return a string representation of the Square object.

        :return: A formatted string describing the square.
        :rtype: str
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.__x, self.__y, self.__size)
