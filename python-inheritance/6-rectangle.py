"""This is the base moduleclass"""


BaseGeometry = _import_('5-base_geometry').BaseGeometry

"""This is an empty class"""


class Rectangle(BaseGeometry):
    """Rectangle subclass"""

    def __init__(self, width, height):
        """calling the validator method"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
