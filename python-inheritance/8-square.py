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
    
    def update(self, *args, **kwargs):
        """These are the arguments
        """
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "width":
                self.width = value
            if key == "height":
                self.height = value
            if key == "x":
                self.id = value
            if key == "y":
                self.id = value

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]



