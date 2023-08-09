"""define thefunction"""
def is_kind_of_class(obj, a_class):
    """check conditions"""
    if isinstance(obj, a_class):
        return True
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False
