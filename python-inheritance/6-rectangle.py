"""This is the base moduleclass"""
BaseGeometry = _import_('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle subclass
    
    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
    """
    def __init__(self, width, height):
        """Initialize a Rectangle instance
        
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

