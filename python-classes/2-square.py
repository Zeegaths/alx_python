""" Class module"""
class Square:
    """ This is a class representing a square"""
    def __init__(self, size=0):        
         """Initializes the size"""
         if type(size) is not int:
              raise TypeError("size must be an integer")
         elif size < 0:
              raise ValueError("size must be >= 0")
         self.__size = size

    def area(self, Square):
         area = self.__size ** 2
         print(area())
         