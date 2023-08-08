""" Class module"""
class Square:
    """ This is a square"""
    def __init__(self, size=0):
         self.__size = size
         self.__size = type(int)
         raise TypeError
    print("size must be an integer")
    def __init__(self, size=0):
         self.__size = size
         if self.__size < 0:
              raise ValueError
         print("size must be >= 0")
    
        

