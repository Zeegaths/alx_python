"""This is an empty class"""
class BaseGeometry:
    """This class is empty"""
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclas__']