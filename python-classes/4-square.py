""" Class module"""
class Square:
    """ This is a class representing a square"""
    def __init__(self, size=0):        
         """Initializes the size"""         
         self.__size = size

    @property        
    def size(self):
         return self.__size

    @size.setter
    def size(self, value):
         if type(value) is not int:
              raise TypeError("size must be an integer")
         elif value < 0:
              raise ValueError("size must be >= 0")
         else:
              self.__size = value
         
    def area(self):
         return int(self.__size ** 2)
    
    def my_print(self):
         if self.__size == 0:
              print()
         else:
              for row in range(self.__size):
                   for column in range(self.__size):
                        print("#")
                   else:
                        print("\n")
         
        
    
    
         