def raise_exception():
    try:
        raise_exception()
    except TypeError():
        print("Exception raised")