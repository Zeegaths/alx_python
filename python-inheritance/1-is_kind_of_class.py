"""define thefunction"""
def is_kind_of_class(obj, a_class):
    """check conditions"""
    if isinstance(obj, a_class):
        return True
    elif issubclass(obj, a_class):
        return True
    else:
        return False
