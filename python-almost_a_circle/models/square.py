"""This is the rectangle module import"""
from models.rectangle import Rectangle

"""This is the square class inheriting from the rectangle"""


class Square(Rectangle):
    """__init method calls the function"""

    def __init__(self, size, x=0, y=0, id=None):
        """calling the super class using the logic of the Rectangle"""
        super().__init__(size, size, x, y, id)
        self.size = size       
    """str method for printing"""

    def __str__(self, Square):
        """defines the format for returning the square attributes"""
        return "[Square] ({}) {}/{} - {}/{}".format(self.id, self.x, self.size)
def update(self, *args, **kwargs):
        """These are the arguments
        """
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

        if kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs: 
                self.x = kwargs["x"]  
            if "y" in kwargs: 
                self.y = kwargs["y"]  