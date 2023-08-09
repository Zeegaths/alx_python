"""defining the function"""
def inherits_from(obj, a_class):
    """initiating conditions"""
    if issubclass(type(obj), a_class):
        return True
    else:
        return False