"""This is an empty class"""
class metaGeometry(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    """This is an empty class"""
class BaseGeometry(metaclass=metaGeometry):
    """This class is empty"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        self.value = value
        self.name = name
        if self.value is not int:
            raise TypeError("{} must be an integer".format(self.name))
        elif self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        else:
            self.value = value