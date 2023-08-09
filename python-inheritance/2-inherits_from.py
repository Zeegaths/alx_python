"""defining the function"""
def inherits_from(obj, a_class):
    """initiating conditions"""
    return issubclass(type(obj), a_class) and type(obj) != a_class